const loadAndProcessData = () =>
  Promise
    .all([
      d3.csv('./data/geometries.csv')
    ])
    .then(([geometriesData]) => {
        residential_geometries_data = geometriesData.filter((data)=> data.unit_usage == "RESIDENTIAL");
        console.log(residential_geometries_data);
    });

loadAndProcessData();