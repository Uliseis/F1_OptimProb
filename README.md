# Formulación de un problema de optimización

Para esta práctica hemos decidido implementar un problema de optimización que busca obtener la vuelta más rapida de clasificación de la Formula 1. Para ellos hemos tenido en cuenta algunos parametros del pilote y del coche.
El circuito escogido para las pruebas es el de Bahrain, el cual hemos dividido en sectores. Para cada sector hemos cogido su longitud, velocidad media de ese sector y el tipo de sector ( curva o recta ). Todos los datos recogidos son tomados con la mayor precisión, la distancia real ( en metros ) y las velocidades medias ( en km/h) de los pilotos en ese orden.

circuit =  [(1100,333.134,'s'), ( 94.53, 100, 't') , (72.38,193.121,'t'), (132.12,225.308,'t'),(491.22,278.417,'s'),
            (151.97,152.888,'t'),(183.74,229.33,'s'),(116.64,225.308,'t'),(123.55,249.448,'t'),(181.68,270.37,'s'),
            (69.69,112.654,'t'),(339.00,211.628,'s'),(103.32,120.701,'t'),(655.09,255.08,'s'),(313.49,209.215,'t'),
            (214.69,280.026,'t'),(236.00,211.88,'t'),(713.44,257.495,'s'),(110.87,162.554,'t')]
         
La función objetivo calcula el tiempo de vuelta para los parametros ("attributes"). Los parametros que se reciben son:

- driver_tyres_treatment: Se corresponde con la capacidad de piloto de cuidar sus ruedas. Los valores que puede tomar son de 0.00 a 10.00. Un mejor cuidado de las ruedas sopone una perdida de velocidad (entre 0.00/+2.00%) a lo largo de la vuelta pero una menor probabilidad de cometer un error ("fail_p", entre un 0.00/+10 %)

- driver_agro: Se corresponde con la agresividad del piloto. Los valores que puede tomar son de 0.00 a 10.00. Un piloto más agresivo irá más rapido (entre un 0.00 y un 1.00%) pero se arriesgará a cometer más errores ("fail_p", entre un 0.00/+2.00%) o chocar ("crash_p", entre un 0.00/+2.00%).

- driver_experience: Se corresponde con la experiencia del piloto. Los valores que puede tomar son de 0.00 a 10.00. Un piloto más experimentado cometerá menos errores ("fail_p", entre el -1.00/+4.00% ) pero por ende irá más lento  o chocar ("crash_p",entre un -0.25/+2.00%).

- car_motor: Se corresponde con la potencia del motor. Los valores que puede tomar son de 0.00 a 10.00. Un coche con un motor más potente correrá más (entre un 0.00/+4.00%) en las rectas, pero pesará más haciendolo más lento en general (entre un 0.00/+1.00%).

- car_aerodynamic_load: Se corresponde con la carga aerodinámica del coche. Los valores que puede tomar son de 0.00 a 10.00. Un coche con una mejor carga aerodinámica irá más rápido en curvas (entre un 0.00/+4.00%) pero más lento en rectas (entre un 0.00/+2.00%).

- car_reliability: Se corresponde con la fiabilidad del coche. Los valores que pueden tomar son de 0.00 a 10.00. Un coche con una mayor fiabilidad será más lento (entre un 0.00/+1.00%) pero menos propenso a sufrir fallos ("fail_p", entre un -1.00/+1.00) y posibles choques ("crash_p", entre un -0.25/+0.25).


Finalmente, calculamos los porcentajes que aplicarán a las velocidades de los sectores ("bonus_global""bonus_turns","bonus_straight", "fail_p", "crash_p"). Seguidamente recorremos el circuito sector a sector. Si el sector es un recta se multpilica su velocidad media por la media de los "bonus_global" y "bonus_straight". Si el sector es una cruva se multiplica su velocidad media por la media de los "bonus_global" y "bonus_turns". Una vez recalculado las velocidades se calcula el tiempo que se tarda en atravesar dicho sector. Además en cada sector hay la posibilidad de cometer un fallo o chocar. En caso de cometer un fallo se penalizaria con 1.5 segudos en el sector. En caso de chocar no será posible completar la vuelta por lo que el tiempo global será infinito.
