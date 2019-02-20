# CiaShopServer
### Service developed to communicate with the Ciashop API.
#### Create by: Marcos Vinicius Ribeiro Silva
#### A permissive license similar to the [BSD 2-Clause License](https://github.com/marcosvsilva/CiaShopServer/blob/master/LICENSE)

Service developed to communicate with the API offered by the ciashop platform to integrate any ERP that uses relational database with the platform.

This service uses external components such as the use of the API and also the relational database to search and write to integrate any ERP.

The architecture defined to treat the external components was defined as:

![alt text](https://github.com/marcosvsilva/CiaShopServer/blob/master/docs/ComponentDiagram.jpg "ComponentDiagram")

The service works with MVCS (Model, View, Controller and Server) architecture and still uses a persistence layer as vision, which can be reimplemented to work with any data architecture of other ERTPs.

![alt text](https://github.com/marcosvsilva/CiaShopServer/blob/master/docs/ClassDiagram.jpg "ClassDiagram")

The project is still in the acceptance and implementation phase. It will be worked on continuous improvement, having the first sprint contemplating all generic architecture.

