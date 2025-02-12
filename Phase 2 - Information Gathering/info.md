## Overview of the Second iTelos Phase

In the second phase of the project, we began by collaboratively discussing the data requirements and available resources. Deciding which datasets to use was not straightforward and required careful consideration of the purpose outlined in the first phase. For instance, we debated whether to create separate datasets for tourist facilities and tourist attractions or to combine them into a single dataset. Ultimately, we decided to merge them under the broader category of **tourist attractions**, aligning with our defined purpose.

Once this decision was made, we divided responsibilities for data collection and cleaning:
- **Amalia** worked on the **Municipalities** and **Waste Production** datasets.
- **Gaudenzia** handled the **Waste** and **Waste Basket** datasets.
- **Yishak** managed the **Tourist Attraction** and **Location** datasets.

This division of labor shaped the structure of the report, with each team member writing sections corresponding to their respective datasets. We focused on detailing the data sources, collection methods, and cleaning processes for each dataset.

### Challenges Faced
One of the main challenges was finding comprehensive data on waste management in the Province of Trento. Waste management regulations vary across municipalities, though the differences are relatively minor. To address this, we referred to the **Dolomiti Ambiente** website, which provides guidelines for Trento and Rovereto. We assumed that other municipalities follow similar regulations to those of the provincial capital.

For spatial data, we primarily relied on **OpenStreetMap**, using **Overpass Turbo** to execute custom queries. OpenStreetMap's collaborative nature offers both advantages and limitations:
- **Advantages**: The data is extensive, accurate, and reliable.
- **Limitations**: Due to its voluntary nature, the data may be partial, with potential gaps or inconsistencies in some areas.

### Future Considerations
If additional data is required as the project progresses, we may reuse datasets from previous course projects, particularly those related to tourism in the Province of Trento.

### Model Revisions
This phase also required us to revise the **Entity-Relationship (ER) model**, as the initial version needed adjustments. Further refinements may be necessary as the project evolves.

### Data Repository
All raw data, pre-processing and querying scripts, and processed datasets are hosted in our [GitHub repository](https://github.com/pariamelle/KGE-Project-Tourism-Waste-Management-in-Trentino.git) under the **Phase Two** section.
