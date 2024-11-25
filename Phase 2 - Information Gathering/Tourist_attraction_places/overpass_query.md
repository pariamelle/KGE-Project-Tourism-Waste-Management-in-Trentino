[out:json];
area["name"="Trento"]["ref:ISTAT"=022205]["boundary"="administrative"]->.searchArea;

(
  
  // Peaks and Viewpoints
  node["natural"="peak"](area.searchArea);
  node["tourism"="viewpoint"](area.searchArea);

  // Lakes and Rivers
  way["natural"="water"]["water"="lake"](area.searchArea);
  relation["natural"="water"]["water"="lake"](area.searchArea);
  way["waterway"="river"](area.searchArea);

  // Nature Reserves and Forests
  relation["boundary"="protected_area"]["protect_class"](area.searchArea);
  way["natural"="wood"](area.searchArea);
  way["landuse"="forest"](area.searchArea);

  // Beaches
  node["natural"="beach"](area.searchArea);
  way["natural"="beach"](area.searchArea);

  // Caves
  node["natural"="cave_entrance"](area.searchArea);

  // Hotels and Accommodations
  node["tourism"="hotel"](area.searchArea);
  node["tourism"="guest_house"](area.searchArea);
  node["tourism"="hostel"](area.searchArea);
  node["tourism"="camp_site"](area.searchArea);
  node["tourism"="caravan_site"](area.searchArea);
  node["tourism"="chalet"](area.searchArea);
  node["tourism"="alpine_hut"](area.searchArea);
  node["building"="hotel"](area.searchArea);

  // Holiday Apartments and Houses
  node["tourism"="apartment"](area.searchArea);
  node["tourism"="holiday_cottage"](area.searchArea);

  // Food and Drink Establishments
  node["amenity"="restaurant"](area.searchArea);
  node["amenity"="cafe"](area.searchArea);
  node["amenity"="bar"](area.searchArea);
  node["amenity"="pub"](area.searchArea);
  node["amenity"="fast_food"](area.searchArea);

  // Cultural Attractions
  node["tourism"="museum"](area.searchArea);
  node["tourism"="artwork"](area.searchArea);
  node["tourism"="gallery"](area.searchArea);
  node["historic"="monument"](area.searchArea);
  node["historic"="memorial"](area.searchArea);
  node["historic"="castle"](area.searchArea);

  // Amusement and Recreational Facilities
  node["tourism"="theme_park"](area.searchArea);
  node["tourism"="zoo"](area.searchArea);
  node["leisure"="amusement_ride"](area.searchArea);
  node["leisure"="miniature_golf"](area.searchArea);
  node["leisure"="park"](area.searchArea);

  // Skiing and Winter Sports
  node["piste:type"="downhill"](area.searchArea);
  node["piste:type"="nordic"](area.searchArea);
  node["piste:type"="snow_park"](area.searchArea);
  way["piste:type"="downhill"](area.searchArea);
  way["piste:type"="nordic"](area.searchArea);

  // Other Natural Attractions
  node["natural"="waterfall"](area.searchArea);
  node["natural"="spring"](area.searchArea);
);

out geom;