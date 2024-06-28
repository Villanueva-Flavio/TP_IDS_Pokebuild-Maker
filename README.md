
# TP grupal de Introducción al desarrollo de software

### Aplicacion: Pokebuild maker

### Estado: Finalizado
![gif](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/440ad541-99c1-4a19-a6c0-082df28d2999)


Estado: Aprobado, pero a que costo?

#### Descripcion:

> Pokebuild maker es un sitio web hecho para aquellos fanáticos de Pokemon que quieran calcular o mostrar sus equipos de los juegos de pokemon. El mismo te permitirá hacer pública el equipo creado y tus pokemons en posesión. En el caso de los pokemons, especificando: Qué pokemon es, Nombre opcional, nivel, y hasta 4 habilidades como los juegos suelen permitir. En el caso de los equipos (builds), se especifica: Los (hasta) 6 pokemons que conforman el equipo


#### Forma de uso:

> Al ingresar al home se visualizarán todas las builds creadas por todos los usuarios con sus respectivos pokemons a la vista

![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/079c3760-b488-4f07-84bc-010fc042b132)

> En el cual si queremos aportar nuestra build tenemos que primero estar registrados, para poder bajo nuestro nombre, publicar nuestros pokemons y builds, por lo que en el boton de agregar (Con forma de pokebola en Home), elegiremos Agregar pokemon

![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/de7c1a69-ae56-482f-ae84-1d34130f7208)

> Una vez que hayamos agregado todos los pokemons con la amplia posibilidad de todos los 1025 pokemons hasta la fecha de este README, y todas sus habilidades, procederemos a crear nuestra build

![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/383b8cdb-4966-4822-a0e6-6bf1f69a0a1e)

> Una vez publicados, vamos a poder realizar nuestras propias modificaciones o eliminaciones de nuestras propias publicaciones
ya sea modificar builds o pokemons, o así mismo eliminarlas.
Podremos tambien visualizar una estadística general de todos los usuarios con la cantidad de pokemons y builds publicadas
	

#### Instalación:

> 1. Primero debés clonar este repositorio con
	`git clone https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker.git`
		
>	2. Y debemos tener instalados Docker y Docker-compose
		Para instalarlo desde linux basta con simplemente:
		`sudo apt update && sudo apt-get install docker docker-compose`
		
>	2. b Para Windows
		`Instalar WSL desde Microsoft Store`
		`Instalar Docker Desktop desde la página web oficial`
			
	
>	3. Para levantar la aplicación debemos considerar que se levantarán 2 contenedores
	    `Database: En el puerto 4000`
		`API/Frontend: En el puerto 5000`
		Por el cual para acceder a nuestra pagina web se realizará mediante
		localhost:5000/
		
>   4. Para levantar los contenedores:
		Situado en la carpeta raíz del repositorio
		(sudo en caso de linux) `docker-compose up`
	    Para cerrarlo bastaría con `CTRL + C` desde el programa
	    o `docker-compose down`
	    
### Pautas de desarrollo:

#### Links:
>	[Ver backlog](https://trello.com/b/MtCIR9PG/copilot-my-beloved)

>    [Ver diseños preliminares](https://miro.com/welcomeonboard/d2drOFdpMkF0cmgwbXJzQW1qcTcxU2YwaVAyRVUxTmlyVlZHTmFBMmtVT1E5RklkRnVwY0JNUEpvVmZlNkZSQXwzMDc0NDU3MzY4MjY1OTI1ODkwfDI=?share_link_id=672689342287)
		
#### Paleta de colores:
|Lightmode  | Darkmode  |
|--|--|
|![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/602ca1a1-087d-43c7-9695-c8f5c0ddec30) #32a852 |![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/92d823ac-00a1-4d48-81d8-c801e6ab054d) #4287f5 |
|![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/5d78ab75-c53f-4dcb-9865-b7381ea2c473) #fcba03 |![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/af75cdbc-11bf-4f04-a207-b96052aae8ba) #eb4034 |
|![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/4acf9c35-94f7-4242-b829-89dea68e11cc) #1e2336 |![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/823d64fa-9356-4620-b57a-a7909d5137eb) #5e00ff |
|![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/2f9cb80a-77d1-42d2-9a2e-91cc36a6229a) #ffeeb2 |![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/d3736d15-a613-4d5c-989f-aee94f9dfbb1) #2f006f |
|![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/4633f4d0-9ef8-44d3-9def-8329cad961b3) #f4f4f4 |![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/186d5b32-fa94-4c91-911f-995ba16f1cdf) #000000 |
|![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/186d5b32-fa94-4c91-911f-995ba16f1cdf) #000000 |![image](https://github.com/Villanueva-Flavio/TP_IDS_Pokebuild-Maker/assets/78744163/316d138c-af41-45e9-8b1d-7c7d1af0c12f) #ffffff |

#### Convenciones de commits:
	[ADD] Commit de adiciones al proyecto
	[DEL] Commit donde se remueven cosas
	[FIX] Commit de bugfixes
	[MER] Commit de merge
	[#10] ID del backlog (Obligatorio)
	Uso de Snake_Case obligatorio
		
#### APIs GET endpoints útiles:
 1. `/api`
    > Este endpoint es el home que nos derivará al resto de endpoints
 1. `/api/pokemons`
    > Este endpoint devolverá todos los pokemons de nuestra base de datos
    > Especificando sus habilidades, id de la pokedex, nombre, nivel y owner
 1. `/api/builds`
    > Este endpoint devolverá todas las builds publicadas por todos los autores
    > Con nombre, owner id y los (hasta) 6 pokemons, incluido su timestamp de creación
 1. `/api/users_profiles`
    > Este endpoint devoverá el nombre, foto, cantidad de pokemons y builds ingresadas de cada usuario
 1. `/api/get_all_pokemons`
    > Este endpoint fetchea el nombre e id de todos los pokemons existentes en la serie
 1. `/api/get_moves/id`
    > Te permitirá obtener los movimientos válidos del pokemon indicado, donde `id` está relacionado a la pokedex
 1. `/api/pokemons_by_user/id`
    > Este endpoint te permitirá obtener todos los pokemons que posee el usuario, con el patron de datos de `/api/pokemons` donde `id` es el id del usuario
 1. `/api/builds_by_user/id`
    > Este endpoint te permitirá obtener un listado de todas las builds que el usuario especificado posee, con el patrón de datos de `/api/builds` donde `id` es el id del usuario
 1. `/api/pokemon/id`
    > Este endpoint te devolverá un pokemon específico cargado en la base de datos donde `id` está relacionado a la tabla, con el patrón de datos de `/api/pokemons` pero siendo un solo pokemon
 1. `/api/build/id`
    > Este endpoint te devolverá una build específica cargada en la base de datos donde `id` está relacionado a la tabla, con el patrón de datos de `/api/builds` pero siendo una sola build
