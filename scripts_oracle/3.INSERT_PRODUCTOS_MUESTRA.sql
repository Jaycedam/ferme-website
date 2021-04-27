DELETE FROM PRODUCTO;
DELETE FROM PROVEEDOR;
DELETE FROM PERSONA;
DELETE FROM MARCA;
DROP SEQUENCE MARCA_SEQ;
DROP SEQUENCE PROVEEDOR_SEQ;
DROP SEQUENCE PRODUCTO_SEQ;
-- MARCA
CREATE SEQUENCE MARCA_SEQ;
INSERT INTO MARCA VALUES(MARCA_SEQ.NEXTVAL, 'SCARAB');
INSERT INTO MARCA VALUES(MARCA_SEQ.NEXTVAL, 'MERC');
INSERT INTO MARCA VALUES(MARCA_SEQ.NEXTVAL, 'FENNEC');
INSERT INTO MARCA VALUES(MARCA_SEQ.NEXTVAL, 'DOMINUS');
INSERT INTO MARCA VALUES(MARCA_SEQ.NEXTVAL, 'OCTANE');
-- PERSONA
INSERT INTO PERSONA VALUES('77658972-1',765432109,1);
INSERT INTO PERSONA VALUES('45321564-5',123456789,2);
-- PROVEEDOR
CREATE SEQUENCE PROVEEDOR_SEQ;
INSERT INTO PROVEEDOR VALUES(PROVEEDOR_SEQ.NEXTVAL,'LIGADECOHETES',19,'77658972-1');
INSERT INTO PROVEEDOR VALUES(PROVEEDOR_SEQ.NEXTVAL,'R3MXBESTOCAR',15,'45321564-5');
-- PRODUCTO
CREATE SEQUENCE PRODUCTO_SEQ;
-- CONTRUCCION
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Siding','Siding fibrocemento 6mm 19x16 3.66m Natural',5590,10,3,'https://i.imgur.com/n9On7uY.jpg',1,1,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Perfil término','Perfil término Vnyl siding 3.80 m',6790,10,3,'https://i.imgur.com/n9On7uY.jpg',1,1,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Balde','Balde construcción 20 litros',4490,10,3,'https://i.imgur.com/n9On7uY.jpg',4,1,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Huincha','Huincha para medir 5 m fibra de vidrio rojo',3790,10,3,'https://i.imgur.com/n9On7uY.jpg',4,1,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Escuadra','Escuadra combinación 12" aluminio negro',3790,10,3,'https://i.imgur.com/n9On7uY.jpg',4,2,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Unión canaleta','Unión canaleta PVC marrón',1490,10,3,'https://i.imgur.com/n9On7uY.jpg',6,2,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Plancha Acanalada','Plancha Acanalada Onda zinc gris 0.35 x 851 x 3000 mm',11530,10,3,'https://i.imgur.com/n9On7uY.jpg',6,2,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Tubo','Tubo bajada PVC 3 m marrón',5524,10,3,'https://i.imgur.com/n9On7uY.jpg',6,2,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Puerta','Puerta Sinfonía HDF 70x200 C/6 Paneles Blanco Prepint',25490,10,3,'https://i.imgur.com/n9On7uY.jpg',8,2,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Ventana','Ventana monolítica aluminio básico 100x100 mate corredera',28990,10,3,'https://i.imgur.com/n9On7uY.jpg',9,2,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Escalera','Escala articulada aluminio 12 peldaños Alto 3,55m. Resistencia 150 Kilos',56552,10,3,'https://i.imgur.com/n9On7uY.jpg',10,2,2);
-- MADERA
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Terciado','Terciado Ranurado T1 12 mm 122 x 244 cm',25990,10,3,'https://i.imgur.com/n9On7uY.jpg',12,1,3);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Madera impregnada','Pino impregnado cobre micronizado 2 x 4 x 3,2 m',5290,10,3,'https://i.imgur.com/n9On7uY.jpg',13,1,3);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Madera seca','Pino dimensionado verde 2 x 3 x 3,20 m',2390,10,3,'https://i.imgur.com/n9On7uY.jpg',13,1,3);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Madera verde','Pino dimensionado verde 2 x 3 x 3,20 m',2390,10,3,'https://i.imgur.com/n9On7uY.jpg',13,1,3);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Armario','Closet 3 puertas pasco 170x79x38 cm café',79990,10,3,'https://i.imgur.com/n9On7uY.jpg',16,1,3);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Librero','Librero 13 repisas 181x44x30cm',59990,10,3,'https://i.imgur.com/n9On7uY.jpg',16,1,3);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Velador','Velador 2 cajones 40x38x64 blanco/oak',69990,10,3,'https://i.imgur.com/n9On7uY.jpg',16,1,3);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Revestimiento','Revestimiento vinílico muro amarillo 1,66 m2',31988,10,3,'https://i.imgur.com/n9On7uY.jpg',15,1,3);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Closet','Closet maria multiuso 1p blanco',129990,10,3,'https://i.imgur.com/n9On7uY.jpg',16,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Escritorio','Escritorio biblioteca',59990,10,3,'https://i.imgur.com/n9On7uY.jpg',16,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Respaldo','Respaldo cama 2 plazas',15900,10,3,'https://i.imgur.com/n9On7uY.jpg',16,2,4);
-- ELECTRICIDAD
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Aspiradora robot','Aspiradora robot Roomba 621',179990,10,3,'https://i.imgur.com/n9On7uY.jpg',17,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cerradura digital','Cerradura digital SG170 Plata',169900,10,3,'https://i.imgur.com/n9On7uY.jpg',17,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Pilas Pack','Pack de 2 pilas alcalinas D 1.5V',4210,10,3,'https://i.imgur.com/n9On7uY.jpg',18,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Lampara','Lámpara escritorio Piccola negra',4490,10,3,'https://i.imgur.com/n9On7uY.jpg',23,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Ampolleta','Ampolleta LED E27 4,5W luz cálida',990,10,3,'https://i.imgur.com/n9On7uY.jpg',24,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Reflector solar','Reflector solar con sensor de movimiento 60W',39990,10,3,'https://i.imgur.com/n9On7uY.jpg',25,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Camara','Cámara sport 2" Full HD',24990,10,3,'https://i.imgur.com/n9On7uY.jpg',22,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Teclado','Teclado multimedia USB 18 teclas ultra',4990,10,3,'https://i.imgur.com/n9On7uY.jpg',22,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Parlante','Parlante Karaoke Ultrascandal',99990,10,3,'https://i.imgur.com/n9On7uY.jpg',22,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Microfono','Micrófono Condensador Grabación Podcasting USB',22990,10,3,'https://i.imgur.com/n9On7uY.jpg',22,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Audifono','Audífonos de estudio K72',45990,10,3,'https://i.imgur.com/n9On7uY.jpg',22,2,4);
-- HERRAMIENTAS
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Soltadora','Soldadora arco manual y TIG 230 amp',225990,10,3,'https://i.imgur.com/n9On7uY.jpg',31,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Betonera','Betonera 150 litros 1,5 HP',549990,10,3,'https://i.imgur.com/n9On7uY.jpg',26,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Ahoyador','Ahoyador 2 tiempos 52 cc 15 cm',239990,10,3,'https://i.imgur.com/n9On7uY.jpg',26,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Picota','Picota acero',19990,10,3,'https://i.imgur.com/n9On7uY.jpg',30,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Taladro','Taladro percutor eléctrico 13 mm 710W',79990,10,3,'https://i.imgur.com/n9On7uY.jpg',32,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Pala','Pala punta de huevo acero',5490,10,3,'https://i.imgur.com/n9On7uY.jpg',30,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Rastrillo','Rastrillo acero',8990,10,3,'https://i.imgur.com/n9On7uY.jpg',30,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Chuzo','Chuzo 1 1/8"x1,75 m acero',17990,10,3,'https://i.imgur.com/n9On7uY.jpg',30,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Compresor','Compresor de aire portátil 2 HP 25 litros',109990,10,3,'https://i.imgur.com/n9On7uY.jpg',26,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Motosierra','Motosierra a gasolina 16" 35,4 cc',152990,10,3,'https://i.imgur.com/n9On7uY.jpg',26,2,4);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Tractor','Tractor 26 hp 764 cc 54"',4299990,10,3,'https://i.imgur.com/n9On7uY.jpg',26,2,4);
-- BAÑO Y FONTANERIA
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Grifo','Monomando lavatorio',14490,10,3,'https://i.imgur.com/n9On7uY.jpg',42,2,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Aireadores','Set 2 Aireadores para baño y cocina',1990,10,3,'https://i.imgur.com/n9On7uY.jpg',40,2,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Juego de tina','Juego de tina ducha almagro',26990,10,3,'https://i.imgur.com/n9On7uY.jpg',40,2,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Flexime metalico','Flexible metálico para ducha 1,5 mt cromado',5990,10,3,'https://i.imgur.com/n9On7uY.jpg',40,2,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Shower','Shower 80x80x200cm',159990,10,3,'https://i.imgur.com/n9On7uY.jpg',41,2,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Papelero','Papelero de Metal 3 Lts Blanco',5990,10,3,'https://i.imgur.com/n9On7uY.jpg',41,2,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Calefont','Calefont Gas licuado 7 litros Tiro Natural',99990,10,3,'https://i.imgur.com/n9On7uY.jpg',46,2,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'WC','WC One Piece Vinciny Ecolé',52990,10,3,'https://i.imgur.com/n9On7uY.jpg',46,2,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Lavamanos','Lavamanos Loza 48x56x45 cm',14990,10,3,'https://i.imgur.com/n9On7uY.jpg',40,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Asiento','Asiento WC Redondo Plástico Blanco',9890,10,3,'https://i.imgur.com/n9On7uY.jpg',40,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Espejo','Espejo para baño 40x50x0,2 cm Blanco',8690,10,3,'https://i.imgur.com/n9On7uY.jpg',40,1,5);
-- Cocina
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Olla presion','Olla a presión 8 litros aluminio',21990,10,3,'https://i.imgur.com/n9On7uY.jpg',48,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Lavaplatos','Mueble lavaplato melamina 120 cm blanco derecho',54990,10,3,'https://i.imgur.com/n9On7uY.jpg',48,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Lavavajillas','Lavavajillas 12C SilencePlus panelable',499990,10,3,'https://i.imgur.com/n9On7uY.jpg',50,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Refrigerador','Refrigerador no frost top freezer 340 litros',299990,10,3,'https://i.imgur.com/n9On7uY.jpg',50,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Microondas','Microondas 17 litros digital',54990,10,3,'https://i.imgur.com/n9On7uY.jpg',50,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cuchillos','Set de 4 cuchillos blade + soporte iman',10890,10,3,'https://i.imgur.com/n9On7uY.jpg',48,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Tabla','Tabla para picar madera 20x30 cm café',4990,10,3,'https://i.imgur.com/n9On7uY.jpg',48,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cucharon','Cuchara de silicona roja',2790,10,3,'https://i.imgur.com/n9On7uY.jpg',48,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Rallador','Rallador multipropósito latón',3390,10,3,'https://i.imgur.com/n9On7uY.jpg',48,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Encendedor','Encendedor cocina tubo grande',3990,10,3,'https://i.imgur.com/n9On7uY.jpg',48,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Pesa','Pesa Digital de Cocina',3990,10,3,'https://i.imgur.com/n9On7uY.jpg',48,1,5);
-- JARDIN
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cortacesped','Cortacésped a gasolina 46 cm 140 cc 5 HP',229990,10,3,'https://i.imgur.com/n9On7uY.jpg',54,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Orillador','Orilladora eléctrica 350 W',25990,10,3,'https://i.imgur.com/n9On7uY.jpg',54,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cortasetos','Cortasetos eléctrico 22" 600 W',59990,10,3,'https://i.imgur.com/n9On7uY.jpg',54,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cosechador de olivos','Cosechador de olivos a gasolina 2,3 HP 52 cc',1590990,10,3,'https://i.imgur.com/n9On7uY.jpg',54,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Inserticida','Insecticida natural para jardín 500 ml líquido',7190,10,3,'https://i.imgur.com/n9On7uY.jpg',60,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Manguera','Set de manguera 18 m verde',13990,10,3,'https://i.imgur.com/n9On7uY.jpg',63,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Gaoteros','Set de goteros botón regulables plástico 5 unidades',1190,10,3,'https://i.imgur.com/n9On7uY.jpg',63,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Abono','Tierra con abono para jardín 35 litros saco',3250,10,3,'https://i.imgur.com/n9On7uY.jpg',62,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Boega','Bodega jardín 192x134x204 cm',399990,10,3,'https://i.imgur.com/n9On7uY.jpg',64,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Organizador','Organizador de jardín 90x39x68 cm Stilo Low',39990,10,3,'https://i.imgur.com/n9On7uY.jpg',59,1,5);
-- FERRETERIA
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Caja Fuerte','Caja fuerte digital 17x20,5x17 cm blanco',24990,10,3,'https://i.imgur.com/n9On7uY.jpg',68,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cerradura Pomo','Cerradura pomo acero antimicrobiana simple paso',5870,10,3,'https://i.imgur.com/n9On7uY.jpg',65,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cerradura manillas','Cerradura acceso 9380 derecha inoxidable',25990,10,3,'https://i.imgur.com/n9On7uY.jpg',65,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cerradura sobreponer','Cerradura sobreponer RIM 321BL',15290,10,3,'https://i.imgur.com/n9On7uY.jpg',65,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cerradura sobreponer','Cerradura sobreponer RIM 321BL',15290,10,3,'https://i.imgur.com/n9On7uY.jpg',65,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Alambre','Alambre de cobre aislado (H07V-U) 1,5 mm2 10 m Blanco',1470,10,3,'https://i.imgur.com/n9On7uY.jpg',70,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cordon','Cordón 2x0,75 mm 10 m  Negro',4990,10,3,'https://i.imgur.com/n9On7uY.jpg',70,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Radio','Radio Auto 2 Din +camara Retroceso+comando Volante',59990,10,3,'https://i.imgur.com/n9On7uY.jpg',73,1,5);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Parlante','Parlante 10cm 4 vias potencia 320w',16990,10,3,'https://i.imgur.com/n9On7uY.jpg',73,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Organizador auto','Organizador de carga 45 kg 19x47x14 cm PVC naranjo',11490,10,3,'https://i.imgur.com/n9On7uY.jpg',73,2,1);
-- Pintura
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Adhesivo','Adhesivo de montaje agarre inmediato 100 ml',4190,10,3,'https://i.imgur.com/n9On7uY.jpg',80,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cola Fria','Cola fría maderas 1 kg',6190,10,3,'https://i.imgur.com/n9On7uY.jpg',80,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Brocha','Brocha multipropósito 2"',2390,10,3,'https://i.imgur.com/n9On7uY.jpg',82,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Pistola pintar','Pistola para pintar control spray 100',69990,10,3,'https://i.imgur.com/n9On7uY.jpg',82,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Rodillo','Rodrillo anti-goteo 23 cm',4490,10,3,'https://i.imgur.com/n9On7uY.jpg',82,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cinta','Cinta para enmascarar 48 mm 40 m',2290,10,3,'https://i.imgur.com/n9On7uY.jpg',82,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Esmalte','Esmalte Sintetico Cereluxe Aquatech Negro 1/4gl',8740,10,3,'https://i.imgur.com/n9On7uY.jpg',86,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Pintura','Pintura látex habitacional blanco 1/4 gl',5140,10,3,'https://i.imgur.com/n9On7uY.jpg',85,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Laca','Laca para madera 1 gl',23690,10,3,'https://i.imgur.com/n9On7uY.jpg',88,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Preservante','Preservante de madera satinado 1 gl',22990,10,3,'https://i.imgur.com/n9On7uY.jpg',88,2,1);
-- DECORACION
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Lampara colgar','Lámpara de colgar tela 1 luz E27 gris',11490,10,3,'https://i.imgur.com/n9On7uY.jpg',90,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Led techo','Apliqué led techo dirigible 1 luz aluminio 10 W blanco',16990,10,3,'https://i.imgur.com/n9On7uY.jpg',90,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Reloj','Reloj pared pajaros de chile',24990,10,3,'https://i.imgur.com/n9On7uY.jpg',91,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Figura dedcorativa','Figura decorativa perro galgo cerámica 26 cm blanco',23990,10,3,'https://i.imgur.com/n9On7uY.jpg',97,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Bonsai','Bonsai 23 cm hoja boj',7990,10,3,'https://i.imgur.com/n9On7uY.jpg',97,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Campana viento','Campana de viento campanas metal',8790,10,3,'https://i.imgur.com/n9On7uY.jpg',97,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Portavelas','Set de portavelas 2 unidades negro',12190,10,3,'https://i.imgur.com/n9On7uY.jpg',97,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Vela','Vela decorativa 7x10 cm crema',4590,10,3,'https://i.imgur.com/n9On7uY.jpg',97,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Mesa de centro','Mesa de centro 120x60x45 cm café',115990,10,3,'https://i.imgur.com/n9On7uY.jpg',97,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'buda deco','Buda decorativo 19,5x14x8 cm poliresina plateado',6490,10,3,'https://i.imgur.com/n9On7uY.jpg',97,2,1);
-- Mobiliario y ordenacion
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Cama americana','Cama americana excellence 1 plaza',114990,10,3,'https://i.imgur.com/n9On7uY.jpg',107,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Sofa','Sofá 2 cuerpo tela 73x145x71 cm',119990,10,3,'https://i.imgur.com/n9On7uY.jpg',103,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Sillon','Sillón de descanso reclinable negro',179990,10,3,'https://i.imgur.com/n9On7uY.jpg',103,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Zapatero','Zapatero 7 repisas 67x30x138 cm Blanco',52990,10,3,'https://i.imgur.com/n9On7uY.jpg',102,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Mesa','Mesa resina look madera 150x80 cm',69990,10,3,'https://i.imgur.com/n9On7uY.jpg',100,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Silla','Silla cannes high 80x43x40 cm blancas',29990,10,3,'https://i.imgur.com/n9On7uY.jpg',101,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Caja Organizadora','Caja organizadora 28 litros 42x32x31 cm transparente',3590,10,3,'https://i.imgur.com/n9On7uY.jpg',104,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Sofa','Sofá 3 cuerpos connor marengo 188x77x76 cm',164990,10,3,'https://i.imgur.com/n9On7uY.jpg',103,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Librero','Librero Essential wengue',109990,10,3,'https://i.imgur.com/n9On7uY.jpg',98,2,1);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Closet','Clóset 4 puertas',84990,10,3,'https://i.imgur.com/n9On7uY.jpg',99,2,1);
-- Climatizacion
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Aire acondicionado','Aire acondicionado Split inverter frío/calor 12.000 BTU AR12TSFZAWK/ZS',452990,10,3,'https://i.imgur.com/n9On7uY.jpg',108,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Ventilador','Ventilador de pedestal 16',21990,10,3,'https://i.imgur.com/n9On7uY.jpg',108,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Enfriador','Enfriador de aire 6 litros 65 W',49390,10,3,'https://i.imgur.com/n9On7uY.jpg',113,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Deshumificador','Deshumidificador 15 litros 2200 W',237990,10,3,'https://i.imgur.com/n9On7uY.jpg',113,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Purificador','Purificador de aire 39 m2',179990,10,3,'https://i.imgur.com/n9On7uY.jpg',113,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Filtros','Filtro hepa purificador wurden',9990,10,3,'https://i.imgur.com/n9On7uY.jpg',113,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Caja Sanitizador','Caja sanitizadora UV',99990,10,3,'https://i.imgur.com/n9On7uY.jpg',113,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Termoventilador','Termoventilador eléctrico 1800 W',12990,10,3,'https://i.imgur.com/n9On7uY.jpg',108,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Calefactor','Calefactor halógeno eléctrico',12990,10,3,'https://i.imgur.com/n9On7uY.jpg',108,1,2);
INSERT INTO PRODUCTO VALUES (PRODUCTO_SEQ.NEXTVAL,'Estufa','Estufa a gas 15 kg GH-42 RED',129990,10,3,'https://i.imgur.com/n9On7uY.jpg',108,1,2);

commit;