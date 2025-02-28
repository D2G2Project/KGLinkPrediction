from rdflib import Graph, URIRef, BNode
from rdflib.namespace import RDF, RDFS, OWL

def materialize_domain_range_triples(g):
    """
    Process owl:unionOf collections to extract domain and range classes
    """
    new_triples = []

    # Process domain relationships
    for s, p, o in g.triples((None, RDFS.domain, None)):
        if isinstance(o, BNode):
            # Check if it's a unionOf collection
            for _, _, union_collection in g.triples((o, OWL.unionOf, None)):
                for class_uri in get_collection_members(g, union_collection):
                    new_triples.append((s, RDFS.domain, class_uri))

                    # Add domain for all subclasses
                    for subclass, _, _ in g.triples((None, RDFS.subClassOf, class_uri)):
                        if not isinstance(subclass, BNode):
                            new_triples.append((s, RDFS.domain, subclass))

    # Process range relationships
    for s, p, o in g.triples((None, RDFS.range, None)):
        if isinstance(o, BNode):
            # Check if it's a unionOf collection
            for _, _, union_collection in g.triples((o, OWL.unionOf, None)):
                for class_uri in get_collection_members(g, union_collection):
                    new_triples.append((s, RDFS.range, class_uri))

    return new_triples

def get_collection_members(g, collection_node):
    """
    Recursively extract IRIs from an RDF collection.
    """
    members = []

    # Check if we're at the end of the list
    if (collection_node, RDF.first, None) in g:
        # Get the first element
        for _, _, first in g.triples((collection_node, RDF.first, None)):
            if not isinstance(first, BNode):
                members.append(first)

        # Recursively process the rest of the list
        for _, _, rest in g.triples((collection_node, RDF.rest, None)):
            if rest != RDF.nil:
                members.extend(get_collection_members(g, rest))

    return members

def get_all_object_properties(g):
    """
    Find all owl:ObjectProperty instances in the graph
    """
    object_properties = []

    for s, p, o in g.triples((None, RDF.type, OWL.ObjectProperty)):
        if not isinstance(s, BNode):
            object_properties.append(s)

    return object_properties

def materialize_subclass_property_relationships(g, property_uri):
    """
    For a given property IRI, find triples where a class is in the domain
    and generate triples connecting all subclasses with appropriate range objects.
    """
    new_triples = []

    # Get all classes in the domain of the property
    domain_classes = []
    for _, _, domain_class in g.triples((property_uri, RDFS.domain, None)):
        if not isinstance(domain_class, BNode):
            domain_classes.append(domain_class)

    # Get all classes in the range of the property
    range_classes = []
    for _, _, range_class in g.triples((property_uri, RDFS.range, None)):
        if not isinstance(range_class, BNode):
            range_classes.append(range_class)

    # For each domain class, find all its subclasses
    all_domain_classes = set(domain_classes)
    for domain_class in domain_classes:
        for subclass, _, _ in g.triples((None, RDFS.subClassOf, domain_class)):
            if not isinstance(subclass, BNode):
                all_domain_classes.add(subclass)

    # Generate triples connecting domain classes with range classes
    for domain_class in all_domain_classes:
        for range_class in range_classes:
            new_triples.append((domain_class, property_uri, range_class))

    return new_triples

def owl_to_ttl_triples_with_materialization(owl_file_path):
    """
    Convert an OWL ontology to TTL format, materializing domain-range relationships
    for all object properties
    """
    # Create an RDF graph
    g = Graph()
    g.parse(owl_file_path)

    # Materialize domain and range relationships
    new_domain_range_triples = materialize_domain_range_triples(g)

    # Add the new triples to the graph
    for s, p, o in new_domain_range_triples:
        g.add((s, p, o))

    # Get all object properties
    object_properties = get_all_object_properties(g)

    # Materialize property relationships for all object properties
    all_property_triples = []
    for prop in object_properties:
        property_triples = materialize_subclass_property_relationships(g, prop)
        all_property_triples.extend(property_triples)

    # Add the new property triples to the graph
    for s, p, o in all_property_triples:
        g.add((s, p, o))

    # Convert to TTL triples
    ttl_triples = []

    for s, p, o in g:
        # Skip blank nodes in output
        if isinstance(s, BNode) or isinstance(o, BNode):
            continue

        # Convert each component to N3 format
        subject = s.n3()
        predicate = p.n3()
        object_str = o.n3()

        # Create triple string
        triple = f"{subject} {predicate} {object_str} ."
        ttl_triples.append(triple)

    # Sort triples for consistency
    ttl_triples.sort()

    return "\n".join(ttl_triples)

def write_ttl_file(owl_file_path, output_path):
    ttl_content = owl_to_ttl_triples_with_materialization(owl_file_path)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(ttl_content)

write_ttl_file("schemaorg.owl", "schemaorg_mat.ttl")