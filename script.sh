helm upgrade selenium-grid --set isolateComponents=true  docker-selenium/charts/selenium-grid/.
helm uninstall selenium-grid 
helm install selenium-grid --set isolateComponents=true  docker-selenium/charts/selenium-grid/.  


# to enable promethus mertic server
helm upgrade selenium-grid --set isolateComponents=true   docker-selenium/charts/selenium-grid/.