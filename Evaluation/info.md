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

### Competency Question 4 (CQ-4)  
**Question:**  
In order to maintain compliance with local regulations, what are the acceptable disposal methods for different waste types?  

```sparql
PREFIX etype: <http://knowdive.disi.unitn.it/etype#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>

SELECT ?wasteName (GROUP_CONCAT(DISTINCT ?disposalMethod; separator=", ") AS ?disposalMethods)
WHERE {
  ?waste rdf:type etype:Waste ;
         etype:has_name ?wasteName ;
         etype:has_disposal_method ?disposalMethod ;
         etype:Category_of ?wasteCat .
  ?wasteCat rdf:type etype:WasteDisposalType ;
            etype:has_name "Paper/Cardboard" .
  FILTER(?disposalMethod != "Organic Fraction (t)")
}
GROUP BY ?wasteName

```


### Competency Question 6 (CQ-6)  
**Question:**  
What special waste disposal facilities are available in Trentino, including their locations, capacities, and the types of waste they manage?

```sparql
PREFIX etype: <http://knowdive.disi.unitn.it/etype#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX geo:   <http://www.opengis.net/ont/geosparql#>

SELECT ?municipalityName ?wasteBasket ?basketLocation ?wasteDisposalType
WHERE {
  # Retrieve the municipality and its name.
  ?municipality rdf:type etype:Municipality ;
                etype:has_name ?municipalityName .
  # Only include municipalities named "Trento".
  FILTER(?municipalityName = "Trento")
  
  # Get waste baskets located in the municipality.
  ?wasteBasket rdf:type etype:WasteBasket ;
               etype:Is_in ?municipality ;
               etype:has_geometry ?basketLocation ;
               etype:Disposes ?wasteDisposal .
  
  # Get the waste disposal type (the type of waste managed).
  ?wasteDisposal rdf:type etype:WasteDisposalType ;
                 etype:has_name ?wasteDisposalType .
  
  # Filter to only include specified waste categories.
  FILTER(?wasteDisposalType IN (
      "Organic", "Paper/Cardboard", "Glass", "Metal", "Plastic", 
      "Textiles", "Electronic Waste", "Wood", "Construction Waste", "Miscellaneous"
  ))
}
ORDER BY ?municipalityName ?wasteDisposalType

```


### Competency Question 8 (CQ-8)  
**Question:**  
During the COVID-19 pandemic, how did visitor fluctuations impact waste production at popular tourist destinations in Trentino? Can we analyze the yearly waste production trends for specific municipalities using the available data?  

```sparql
PREFIX etype: <http://knowdive.disi.unitn.it/etype#>
PREFIX rdf:   <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd:   <http://www.w3.org/2001/XMLSchema#>

SELECT ?municipalityName ?attractionCount ?wasteCategory 
       ((?w2020 - ?w2018) AS ?diff_2020_2018) ((?w2022 - ?w2020) AS ?diff_2022_2020)
WHERE {
  { # Top 10 municipalities by attractions
        SELECT ?municipality ?municipalityName (COUNT(?attraction) AS ?attractionCount) {
      ?municipality a etype:Municipality ; etype:has_name ?municipalityName .
      ?attraction a etype:TouristAttraction ; etype:Located_in ?municipality .
    }
    GROUP BY ?municipality ?municipalityName 
    ORDER BY DESC(?attractionCount) LIMIT 10
  }
  
  # Unified waste data collection for all years
  OPTIONAL { 
    SELECT ?municipality ?wasteCategory 
        (SUM(xsd:decimal(REPLACE(REPLACE(STR(?q2018), "\\.", ""), ",", "."))) AS ?w2018)
        (SUM(xsd:decimal(REPLACE(REPLACE(STR(?q2020), "\\.", ""), ",", "."))) AS ?w2020)
        (SUM(xsd:decimal(REPLACE(REPLACE(STR(?q2022), "\\.", ""), ",", "."))) AS ?w2022)
    WHERE {
      { ?w a etype:WasteProduction ; etype:Generated_by ?municipality ; etype:has_year "2018" ; 
          etype:has_quantity ?q2018 ; etype:Category_of/etype:has_name ?wasteCategory . }
      UNION
      { ?w a etype:WasteProduction ; etype:Generated_by ?municipality ; etype:has_year "2020" ; 
          etype:has_quantity ?q2020 ; etype:Category_of/etype:has_name ?wasteCategory . }
      UNION
      { ?w a etype:WasteProduction ; etype:Generated_by ?municipality ; etype:has_year "2022" ; 
          etype:has_quantity ?q2022 ; etype:Category_of/etype:has_name ?wasteCategory . }
      FILTER(?wasteCategory IN ("Organic", "Paper/Cardboard", "Glass", "Plastic"))
    }
    GROUP BY ?municipality ?wasteCategory
  }
  FILTER(BOUND(?w2018) && BOUND(?w2020)) # Ensure required years exist
}
ORDER BY DESC(?attractionCount) ?municipalityName ?wasteCategory

```

