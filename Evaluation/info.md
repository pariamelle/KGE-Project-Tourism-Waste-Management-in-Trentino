## Evaluation

### EType Level  
**Coverage Calculation:**  
CovE(CQE) = (CQe ∩ Te) / CQe = 6 / 9 ≈ 0.7

### Property Level  
**Coverage Calculation:**  
CovP(CQp) = (CQp ∩ Tp) / CQp = 30 / 42 ≈ 0.7

### EType Level  
**Coverage Calculation:**  
CovE(ROE) = (ROe ∩ Te) / ROe = 6 / 6 = 1

### Property Level  
**Coverage Calculation:**  
CovP(ROp) = (ROp ∩ Tp) / ROp = 17 / 17 = 1

### Entity Connectivity (EC)  
**Overall Calculation:**  
EC(KG) = 1 + 1 + 1.5 + 2 + 1 + 1 + 2 = 9.5

### Property Connectivity (PC)  
**Overall Calculation:**  
PC(KG) = 7


## Competency Questions answered

### Competency Question 1 (CQ-1)  
**Question:**  
As a policy maker or researcher evaluating waste management, what is the total amount of a specific type of waste generated in municipalities that host certain types of tourist attractions during a given year?

```sparql
PREFIX etype: <http://knowdive.disi.unitn.it/etype#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd:   <http://www.w3.org/2001/XMLSchema#>

SELECT ?municipalityName ?wasteCategory 
       (SUM(xsd:decimal(REPLACE(REPLACE(STR(?wasteQuantity), "\\.", ""), ",", "."))) AS ?totalWaste)
WHERE {
  # Get the municipality and its name.
  ?municipality rdf:type etype:Municipality ;
                etype:has_name ?municipalityName .
  
  # Get a tourist attraction in the municipality.
  ?attraction rdf:type etype:TouristAttraction ;
              etype:Located_in ?municipality ;
              etype:has_type ?attractionType .
  # Accept attractions with a type containing "skiing" (case-insensitive).
  FILTER(regex(?attractionType, "skiing", "i"))
  
  # Get waste production data for the municipality for the year 2022.
  ?wasteProduction rdf:type etype:WasteProduction ;
                   etype:Generated_by ?municipality ;
                   etype:has_quantity ?wasteQuantity ;
                   etype:has_year "2022" ;
                   etype:Category_of ?wasteDisposal .
  
  # Get the waste category.
  ?wasteDisposal rdf:type etype:WasteDisposalType ;
                 etype:has_name ?wasteCategory .
  
  # Restrict results to only the "Plastic" category.
  FILTER(?wasteCategory = "Plastic")
}
GROUP BY ?municipalityName ?wasteCategory
ORDER BY DESC(?totalWaste)

```

### Competency Question 2 (CQ-2)  
**Question:**  
While enjoying winter sports, where can I find the nearest recycling bins, and what types of waste can I dispose of in these bins?  

```sparql
PREFIX rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX etype: <http://knowdive.disi.unitn.it/etype#>
PREFIX geo:   <http://www.opengis.net/ont/geosparql#>
PREFIX geof:  <http://www.opengis.net/def/function/geosparql/>
PREFIX uom: <http://www.opengis.net/def/uom/OGC/1.0/>


SELECT ?amenity ?distance ?Location ?wasteTypeName ?wasteTypeDescription 
WHERE {
  BIND("recycling" AS ?amenity)
  BIND("POINT (11.0308 45.9881)"^^geo:wktLiteral AS ?userLocation)
  VALUES ?wasteTypeName { "Organic" "Paper/Cardboard" "Glass" "Metal" "Plastic" }
  
  ?recyclingBin rdf:type etype:WasteBasket ;
                etype:has_amenity ?amenity ;
                etype:has_geometry ?binGeometry ;
                etype:Disposes ?wasteType ;
                etype:Is_in ?municipality .
  ?municipality etype:has_name ?municipalityName .
  ?wasteType etype:has_name ?wasteTypeName ;
             etype:has_description ?wasteTypeDescription .
     BIND(STRDT(?binGeometry, geo:wktLiteral) AS ?binGeometryLiteral)

  BIND(geof:distance(?userLocation, ?binGeometryLiteral, uom:metre) AS ?distance)
    BIND(?binGeometry AS ?Location )
    
}
ORDER BY ?distance

```

```sparql
```

### Competency Question 4 (CQ-4)  
**Question:**  
In order to maintain compliance with local regulations, what are the acceptable disposal methods for different waste types?  

```sparql
```


### Competency Question 6 (CQ-6)  
**Question:**  
What special waste disposal facilities are available in Trentino, including their locations, capacities, and the types of waste they manage?

```sparql
```


### Competency Question 8 (CQ-8)  
**Question:**  
During the COVID-19 pandemic, how did visitor fluctuations impact waste production at popular tourist destinations in Trentino? Can we analyze the yearly waste production trends for specific municipalities using the available data?  

```sparql
```

