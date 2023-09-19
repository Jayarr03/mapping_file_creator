import pandas as pd

def trustzones():
    return (
    """trustzones:
  - label:   Public Cloud
    type:    Public Cloud
    id:      b61d6911-338d-46a8-9f39-8dcd24abfe91
    default: true

  - label:  Private Secured Cloud
    type:   Private Secured
    id:     2ab4effa-40b7-4cd2-ba81-8247d29a6f2d

  - label:  Internet
    type:   Internet
    id:     f0ba7722-39b6-4c81-8290-a30a248bb8d9"""
    )

def component_intro():
    return """
    
components:
    ################################################################################################
    #   Azure STENCILS
    ################################################################################################"""

def component_mappings(incoming_name, iriusrisk_component):
    return f"""
      - label: {incoming_name}
        type: {iriusrisk_component}
    """

def dataflows():
    return """
    dataflows: []"""

data = pd.read_csv(r'C:\Users\jrabe_iriusrisk\PycharmProjects\mapping_file_creator\mappings.csv')  # Replace 'your_spreadsheet.csv' with the actual file name and path

# Create a YAML file and write the content to it
with open('output.yaml', 'w') as file:
    file.write(trustzones())
    file.write(component_intro())
    for index, row in data.iterrows():
        incoming_name = str(row['incoming_name'])
        iriusrisk_component = str(row['iriusrisk_component'])
        file.write(component_mappings(incoming_name, iriusrisk_component))
    file.write(dataflows())
