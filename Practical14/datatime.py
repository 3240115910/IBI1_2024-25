# change work dictionary
import xml.dom.minidom
from datetime import datetime
import os
os.chdir(r'C:\Users\张嘉芮1\Desktop\IBI1\IBI1_2024-25\Practical14')

# defined a new function and parse XML file
# Create a dictionary to store the analysis results of three ontologies
# Each ontology corresponds to a sub dictionary that records specific information
def parse_with_dom(xml_file):
    start_time = datetime.now()
    dom = xml.dom.minidom.parse(xml_file)
    results = {
        'molecular_function': {'max_depth': 0, 'term_id': None, 'term_name': None},
        'biological_process': {'max_depth': 0, 'term_id': None, 'term_name': None},
        'cellular_component': {'max_depth': 0, 'term_id': None, 'term_name': None}
    }
    # Get all term and namespace nodes
    terms = dom.getElementsByTagName('term')
    for term in terms:
        namespace_nodes = term.getElementsByTagName('namespace')
        if not namespace_nodes:
            continue
        namespace = namespace_nodes[0].firstChild.nodeValue.strip()
        if namespace not in results:
            continue
        # Get term id and name 
        # count the number of is_a  
        # If the is_a quantity of the current term is greater than the maximum recorded value, update the result
        term_id = term.getElementsByTagName('id')[0].firstChild.nodeValue.strip()
        term_name = term.getElementsByTagName('name')[0].firstChild.nodeValue.strip()
        is_a_count = len(term.getElementsByTagName('is_a'))
        if is_a_count > results[namespace]['max_depth']:
            results[namespace]['max_depth'] = is_a_count
            results[namespace]['term_id'] = term_id
            results[namespace]['term_name'] = term_name
    end_time = datetime.now()
    execution_time = end_time - start_time  
    return results, execution_time

import xml.sax
from datetime import datetime
# Initialize various state variables
class GOHandler(xml.sax.ContentHandler):
    def __init__(self):
        self.current_element = ""
        self.namespace = ""
        self.term_id = ""
        self.term_name = ""
        self.is_a_count = 0
        self.results = {
            'molecular_function': {'max_depth': 0, 'term_id': None, 'term_name': None},
            'biological_process': {'max_depth': 0, 'term_id': None, 'term_name': None},
            'cellular_component': {'max_depth': 0, 'term_id': None, 'term_name': None}
        }
    
    def startElement(self, name, attrs):
        self.current_element = name
        if name == "term":
            self.term_id = ""
            self.term_name = ""
            self.namespace = ""
            self.is_a_count = 0
    # Multiple calls when processing element content
    def characters(self, content):
        if self.current_element == "id":
            self.term_id += content.strip()
        elif self.current_element == "name":
            self.term_name += content.strip()
        elif self.current_element == "namespace":
            self.namespace += content.strip()
    # Call when encountering the end tag
    def endElement(self, name):
        if name == "is_a":
            self.is_a_count += 1
        elif name == "term":
            if self.namespace in self.results:
                if self.is_a_count > self.results[self.namespace]['max_depth']:
                    self.results[self.namespace]['max_depth'] = self.is_a_count
                    self.results[self.namespace]['term_id'] = self.term_id
                    self.results[self.namespace]['term_name'] = self.term_name

def parse_with_sax(xml_file):
    start_time = datetime.now()
    
    handler = GOHandler()
    parser = xml.sax.make_parser()
    parser.setContentHandler(handler)
    parser.parse(xml_file)
    # count the time
    end_time = datetime.now()
    execution_time = end_time - start_time
    
    return handler.results, execution_time

def main():
    xml_file = "go_obo.xml"
    
    print("Processing with DOM API...")
    dom_results, dom_time = parse_with_dom(xml_file)
    
    print("\nProcessing with SAX API...")
    sax_results, sax_time = parse_with_sax(xml_file)
    
    # print the results of DOM and SAX 
    print("\nDOM API Results:")
    for namespace, data in dom_results.items():
        print(f"{namespace.replace('_', ' ').title()}:")
        print(f"  Term ID: {data['term_id']}")
        print(f"  Term Name: {data['term_name']}")
        print(f"  Maximum Depth (is_a count): {data['max_depth']}\n")

    print("\nSAX API Results:")
    for namespace, data in sax_results.items():
        print(f"{namespace.replace('_', ' ').title()}:")
        print(f"  Term ID: {data['term_id']}")
        print(f"  Term Name: {data['term_name']}")
        print(f"  Maximum Depth (is_a count): {data['max_depth']}\n")
    
    # Compare and display the execution time of two methods
    # Explain which method is faster
    print("\nExecution Time Comparison:")
    print(f"DOM API: {dom_time.total_seconds():.4f} seconds")
    print(f"SAX API: {sax_time.total_seconds():.4f} seconds")
    if dom_time < sax_time:
        print("\n# DOM API was faster in this execution.")
    else:
        print("\n# SAX API was faster in this execution.")
if __name__ == "__main__":
    main()