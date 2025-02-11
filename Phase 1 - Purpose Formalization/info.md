\subsection{Overview of the first iTelos phase}

In the initial phase of this project, our focus was to clearly define the project’s purpose and identify key personas and scenarios likely to interact with the Knowledge Graph (KG). These personas include tourists visiting Trentino for leisure, analysts from the Province of Trento, and researchers from external institutions (such as FBK) who may use the KG to access information related to waste management and its connection to tourism. Guided by the competency questions, we then identified common, core, and contextual entities - along with their relevant properties - to structure the KG. This preliminary framework remains flexible, allowing us to adjust it based on data availability and ensuring the project's feasibility throughout later stages.
\newline 
In this phase, we adopted the so-called Middle-out approach, considering both the knowledge layer and the data layer to facilitate easy data adaptation and knowledge modeling.
\newline 
As a preliminary step, we collaboratively reviewed the data resources provided by our instructor:
\begin{itemize}
\item A comprehensive \href{https://datascientiafoundation.github.io/LiveData-KGE/datasets/tourist-facilities/}{Knowledge Graph on tourism data}
\item The \href{https://www.catasto-rifiuti.isprambiente.it/index.php?pg=comune&aa=2020&regid=04022&cerca=cerca&p=1&width=1920&height=1200&advice=si}{ISPRA website}, which provided aggregated data on waste production per municipality and the locations of facilities for handling specific types of waste (e.g., special waste). Waste production data spans from 2010 to 2022, adding a valuable temporal dimension which helped to frame our Domain of Interest.
\end{itemize}
After analyzing these sources, we brainstormed additional datasets that could strengthen the KG’s depth and utility. Key suggestions included
\begin{itemize}
\item Data on local waste disposal policies: Useful for managers of tourist facilities who require up-to-date disposal guidelines (Proposed by Gaudenzia).
\item Data on public waste bin locations: Important for tourists who may need guidance on waste disposal options in unfamiliar areas (Proposed by Amalia).
\item Real-time, geolocated data on tourist presence: Valuable for facility managers to optimize waste bin placement and collection logistics (Proposed by Yishak).  
\end{itemize}
However, acquiring this additional data may present challenges. No centralized collection of waste disposal policies exists, so manual entry may be necessary. For public waste bin data, official sources are unavailable, so we considered relying on crowdsourced platforms like Overpass Turbo. 
\newline
After gaining a general understanding of the available data sources, we shifted our focus to envisioning the final product and identifying potential personas and scenarios, as well as competency questions. For personas development, we leveraged our local experience and knowledge of the area, including our understanding of the types of tourists who frequent Trentino—primarily outdoor sports enthusiasts. We considered their possible needs and the types of waste-related information that would interest them, concluding that their primary concern would likely be access to disposal facilities. This approach also applied to tourist facility owners, who share similar concerns around waste disposal options for their guests. On the other hand, data such as annual waste production by municipality and ISPRA’s other aggregated metrics, which are less relevant to the general public, are highly useful for policymakers, waste management authorities, and city administrators interested in broader environmental management. Lastly, we recognized that researchers could also benefit significantly from the KG, particularly given the temporal data dimensions, which support more in-depth analysis. While developing the Purpose Formalization Sheet and the Entity-Relationship Model, we took into consideration several reference context schemas, and particularly Schema.org. 
\newline
Throughout this phase, each team member contributed to defining the project’s purpose and domain of interest, as well as discussing the available data sources. Amalia and Gaudenzia identified personas, scenarios, and competency questions, creating the concept identification table. Gaudenzia and Yishak developed the Entity-Relationship (ER) schema using the IDEF1X notation, as recommended. Yishak managed all layout and formatting in LaTeX, while Amalia updated the repository on GitHub.


