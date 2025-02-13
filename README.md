
# KGE Project - Tourism and Waste Management in Trentino


This repository contains the iTelos project for the **Knowledge Graph Engineering** course (2024/25) taught by Professors Fausto Giunchiglia, Simone Bocca, and Mayukh Bagchi at the University of Trento. The project was developed by Gaudenzia Genoni, Maria Amalia Pelle, and Yishak Tadele Nigatu for the Master's in Data Science program.

## Purpose and Domain
**Objective:** Offer comprehensive information regarding waste management and its relationship with tourism.  
**Geographic Focus:** Trentino Province (46°04′00″N, 11°07′00″E)  
**Temporal Coverage:** 2014-2022  

## Data Sources
- 🗺️ [**OpenStreetMap**](https://www.openstreetmap.org/): Geospatial data for waste baskets and tourist attractions
- ♻️ [**Dolomiti Ambiente**](https://dolomitiambiente.it/it/): Waste disposal types and management practices
- 📊 [**ISPRA**](https://www.isprambiente.gov.it/it): Annual municipal waste production data
- 📈 [**ISTAT**](https://www.istat.it/): Demographic statistics and municipal boundaries

## Reference Schema
Alignment with [schema.org](https://schema.org) vocabulary for entity modeling.

## Core Components
1. **Conceptual Models**
   - [Entity-Relationship (ER) Model](https://github.com/pariamelle/KGE-Project-Tourism-Waste-Management-in-Trentino/blob/main/Phase%201%20-%20Purpose%20Formalization/ER_model_2.svg)
   - Enhanced Entity-Relationship (EER) Model
2. **Knowledge Representation**
   - Teleontology using kTelos methodology
   - Schema alignment
3. **Implementation**
   - Protégé
   - Karma data mapping
  
## Evaluation
- **Metrics:** Purpose satisfaction (70%), Reusability index (100%)
- **Validation:** All competency questions answered, with varying degrees of granularity
- **Performance:** Average query response time < 1.2s

## Example SPARQL Query
**Competency Question:** Find organic waste facilities within 5 km of ski tourist attractions in Folgaria.  
```sparql
PREFIX etype: <http://knowdive.disi.unitn.it/etype#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX geo:   <http://www.opengis.net/ont/geosparql#>
PREFIX geof:  <http://www.opengis.net/def/function/geosparql/>
PREFIX uom:   <http://www.opengis.net/def/uom/OGC/1.0/>

SELECT ?municipalityName ?attractionName ?attractionType ?attractionLocation ?basketLocation ?wasteDisposalType ?distance 
WHERE {
  # Retrieve tourist attractions located in Folgaria.
  ?attraction rdf:type etype:TouristAttraction ;
              etype:has_type ?attractionType ;
              etype:has_name ?attractionName ;
              etype:has_geometry ?attractionLocation ;
              etype:Located_in ?municipality .
  ?municipality etype:has_name ?municipalityName .
  FILTER(?municipalityName = "Folgaria")
  
  # Filter so that the attraction's type is exactly "skiing".
  FILTER(?attractionType = "skiing")
  
  # Optionally include additional tourist attraction attributes.
  OPTIONAL { ?attraction etype:has_description ?attractionDescription . }
  
  # For each attraction, find waste baskets (recycling facilities).
  ?wasteBasket rdf:type etype:WasteBasket ;
               etype:has_amenity "recycling" ;
               etype:has_geometry ?basketLocation ;
               etype:Disposes ?wasteDisposal .
  
  # Compute the distance (in meters) from the attraction to the waste basket.
  BIND(geof:distance(?attractionLocation, ?basketLocation, uom:metre) AS ?distance)
  
  # Only include waste baskets within 5000 meters.
  FILTER(?distance <= 5000)
  
  # Retrieve the waste disposal type name.
  ?wasteDisposal rdf:type etype:WasteDisposalType ;
                 etype:has_name ?wasteDisposalType .
  
  # Filter to only include waste baskets that accept Organic waste.
  FILTER(?wasteDisposalType = "Organic")
}
ORDER BY ASC(?distance)

```

## Team

<!-- Empty line before table -->
    
| Member                   | Contribution Area       |
|:-------------------------|:------------------------|
| Gaudenzia Genoni         | Knowledge Engineer      |
| Maria Amalia Pelle       | Project Manager    |
| Yishak Tadele Nigatu     | Data Scientist      |

## License
[![CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

**Hosted on GitHub Pages** · Last updated: Feb 2025  
[View Project Documentation](Documentation/KGE_Group_9_Report.pdf) · [Report Issue](https://github.com/pariamelle/KGE-Project-Tourism-Waste-Management-in-Trentino/issues)
