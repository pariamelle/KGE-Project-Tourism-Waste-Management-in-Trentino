
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

## Methodology: Core Components
1. **Conceptual Models**
   - Entity-Relationship (ER) Model
   - Enhanced Entity-Relationship (EER) Model
2. **Knowledge Representation**
   - Teleontology using kTelos methodology
   - Schema alignment
3. **Implementation**
   - Protégé
   - Karma data mapping
  
## Evaluation
- **Metrics:** Purpose satisfaction (85%), Reusability index (92%)
- **Validation:** 15/20 competency questions fully answered
- **Performance:** Average query response time < 1.2s

## Example SPARQL Query
**Competency Question:** Find ski attractions in Folgaria with nearby organic waste facilities (≤5km)

```sparql
PREFIX etype: <http://knowdive.disi.unitn.it/etype#>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX geo: <http://www.opengis.net/ont/geosparql#>
PREFIX geof: <http://www.opengis.net/def/function/geosparql/>
PREFIX uom: <http://www.opengis.net/def/uom/OGC/1.0/>

SELECT ?municipalityName ?attractionName ?distance WHERE {
  ?attraction rdf:type etype:TouristAttraction ;
    etype:has_type "skiing" ;
    etype:has_name ?attractionName ;
    etype:has_geometry ?attractionLoc ;
    etype:Located_in [ etype:has_name "Folgaria" ].
  
  ?wasteBasket rdf:type etype:WasteBasket ;
    etype:has_amenity "recycling" ;
    etype:has_geometry ?basketLoc ;
    etype:Disposes [ etype:has_name "Organic" ].
  
  BIND(geof:distance(?attractionLoc, ?basketLoc, uom:metre) AS ?distance)
  FILTER(?distance <= 5000)
}
ORDER BY ASC(?distance)
```

## Team

<!-- Empty line before table -->
    
| Member                   | Contribution Area       |
|:-------------------------|:------------------------|
| Gaudenzia Genoni         | Data Modeling           |
| Maria Amalia Pelle       | Ontology Development    |
| Yishak Tadele Nigatu     | Query Optimization      |

## License
[![CC BY 4.0](https://img.shields.io/badge/License-CC_BY_4.0-lightgrey.svg)](https://creativecommons.org/licenses/by/4.0/)

---

**Hosted on GitHub Pages** · Last updated: Feb 2025  
[View Project Documentation](Documentation/2024___2025_KGE_Project_Report_Template.pdf) · [Report Issue](https://github.com/pariamelle/KGE-Project-Tourism-Waste-Management-in-Trentino/issues)
