alter table producto modify precio_proveedor default 0;

-- MARCA
INSERT INTO MARCA (MARCA) VALUES('SCARAB');
INSERT INTO MARCA (MARCA) VALUES('MERC');
INSERT INTO MARCA (MARCA) VALUES('FENNEC');
INSERT INTO MARCA (MARCA) VALUES('DOMINUS');
INSERT INTO MARCA (MARCA) VALUES('OCTANE');
-- PERSONA
INSERT INTO PERSONA VALUES('77658972-1',765432109,2);
INSERT INTO PERSONA VALUES('45321564-5',123456789,3);
-- PROVEEDOR
INSERT INTO PROVEEDOR (NOMBRE_EMPRESA, ID_RUBRO, RUT_PERSONA) VALUES('LIGADECOHETES',19,'77658972-1');
INSERT INTO PROVEEDOR (NOMBRE_EMPRESA, ID_RUBRO, RUT_PERSONA) VALUES('R3MXBESTOCAR',15,'45321564-5');
-- PRODUCTO
-- CONTRUCCION
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Siding','Siding fibrocemento 6mm 19x16 3.66m Natural',5590,10,3,'products/1.jpg',1,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Perfil término','Perfil término Vnyl siding 3.80 m',6790,10,3,'products/1.jpg',1,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Balde','Balde construcción 20 litros',4490,10,3,'products/1.jpg',4,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Huincha','Huincha para medir 5 m fibra de vidrio rojo',3790,10,3,'products/1.jpg',4,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Escuadra','Escuadra combinación 12" aluminio negro',3790,10,3,'products/1.jpg',4,100,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Unión canaleta','Unión canaleta PVC marrón',1490,10,3,'products/1.jpg',6,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Plancha Acanalada','Plancha Acanalada Onda zinc gris 0.35 x 851 x 3000 mm',11530,10,3,'products/1.jpg',6,100,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Tubo','Tubo bajada PVC 3 m marrón',5524,10,3,'products/1.jpg',6,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Puerta','Puerta Sinfonía HDF 70x200 C/6 Paneles Blanco Prepint',25490,10,3,'products/1.jpg',8,100,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Ventana','Ventana monolítica aluminio básico 100x100 mate corredera',28990,10,3,'products/1.jpg',9,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Escalera','Escala articulada aluminio 12 peldaños Alto 3,55m. Resistencia 150 Kilos',56552,10,3,'products/1.jpg',10,100,2);
-- MADERA
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Terciado','Terciado Ranurado T1 12 mm 122 x 244 cm',25990,10,3,'products/1.jpg',12,100,3);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Madera impregnada','Pino impregnado cobre micronizado 2 x 4 x 3,2 m',5290,10,3,'https://i.imgur.com/n9100On7uY.jpg',13,100,3);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Madera seca','Pino dimensionado verde 2 x 3 x 3,20 m',2390,10,3,'products/1.jpg',13,100,3);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Madera verde','Pino dimensionado verde 2 x 3 x 3,20 m',2390,10,3,'products/1.jpg',13,100,3);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Armario','Closet 3 puertas pasco 170x79x38 cm café',79990,10,3,'products/1.jpg',16,100,3);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Librero','Librero 13 repisas 181x44x30cm',59990,10,3,'products/1.jpg',16,100,3);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Velador','Velador 2 cajones 40x38x64 blanco/oak',69990,10,3,'products/1.jpg',16,101,3);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Revestimiento','Revestimiento vinílico muro amarillo 1,66 m2',31988,10,3,'products/1.jpg',15,101,3);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Closet','Closet maria multiuso 1p blanco',129990,10,3,'products/1.jpg',16,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Escritorio','Escritorio biblioteca',59990,10,3,'products/1.jpg',16,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Respaldo','Respaldo cama 2 plazas',15900,10,3,'products/1.jpg',16,101,4);
-- ELECTRICIDAD
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Aspiradora robot','Aspiradora robot Roomba 621',179990,10,3,'products/1.jpg',17,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cerradura digital','Cerradura digital SG170 Plata',169900,10,3,'products/1.jpg',17,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Pilas Pack','Pack de 2 pilas alcalinas D 1.5V',4210,10,3,'products/1.jpg',18,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Lampara','Lámpara escritorio Piccola negra',4490,10,3,'products/1.jpg',23,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Ampolleta','Ampolleta LED E27 4,5W luz cálida',990,10,3,'products/1.jpg',24,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Reflector solar','Reflector solar con sensor de movimiento 60W',39990,10,3,'products/1.jpg',25,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Camara','Cámara sport 2" Full HD',24990,10,3,'products/1.jpg',22,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Teclado','Teclado multimedia USB 18 teclas ultra',4990,10,3,'products/1.jpg',22,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Parlante','Parlante Karaoke Ultrascandal',99990,10,3,'products/1.jpg',22,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Microfono','Micrófono Condensador Grabación Podcasting USB',22990,10,3,'products/1.jpg',22,100,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Audifono','Audífonos de estudio K72',45990,10,3,'products/1.jpg',22,100,4);
-- HERRAMIENTAS
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Soltadora','Soldadora arco manual y TIG 230 amp',225990,10,3,'products/1.jpg',31,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Betonera','Betonera 150 litros 1,5 HP',549990,10,3,'products/1.jpg',26,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Ahoyador','Ahoyador 2 tiempos 52 cc 15 cm',239990,10,3,'products/1.jpg',26,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Picota','Picota acero',19990,10,3,'products/1.jpg',30,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Taladro','Taladro percutor eléctrico 13 mm 710W',79990,10,3,'products/1.jpg',32,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Pala','Pala punta de huevo acero',5490,10,3,'products/1.jpg',30,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Rastrillo','Rastrillo acero',8990,10,3,'products/1.jpg',30,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Chuzo','Chuzo 1 1/8"x1,75 m acero',17990,10,3,'products/1.jpg',30,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Compresor','Compresor de aire portátil 2 HP 25 litros',109990,10,3,'products/1.jpg',26,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Motosierra','Motosierra a gasolina 16" 35,4 cc',152990,10,3,'products/1.jpg',26,101,4);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Tractor','Tractor 26 hp 764 cc 54"',4299990,10,3,'products/1.jpg',26,101,4);
-- BAÑO Y FONTANERIA
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Grifo','Monomando lavatorio',14490,10,3,'products/1.jpg',42,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Aireadores','Set 2 Aireadores para baño y cocina',1990,10,3,'products/1.jpg',40,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Juego de tina','Juego de tina ducha almagro',26990,10,3,'products/1.jpg',40,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Flexime metalico','Flexible metálico para ducha 1,5 mt cromado',5990,10,3,'products/1.jpg',40,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Shower','Shower 80x80x200cm',159990,10,3,'products/1.jpg',41,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Papelero','Papelero de Metal 3 Lts Blanco',5990,10,3,'products/1.jpg',41,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Calefont','Calefont Gas licuado 7 litros Tiro Natural',99990,10,3,'products/1.jpg',46,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('WC','WC One Piece Vinciny Ecolé',52990,10,3,'products/1.jpg',46,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Lavamanos','Lavamanos Loza 48x56x45 cm',14990,10,3,'products/1.jpg',40,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Asiento','Asiento WC Redondo Plástico Blanco',9890,10,3,'products/1.jpg',40,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Espejo','Espejo para baño 40x50x0,2 cm Blanco',8690,10,3,'products/1.jpg',40,100,5);
-- Cocina
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Olla presion','Olla a presión 8 litros aluminio',21990,10,3,'products/1.jpg',48,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Lavaplatos','Mueble lavaplato melamina 120 cm blanco derecho',54990,10,3,'products/1.jpg',48,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Lavavajillas','Lavavajillas 12C SilencePlus panelable',499990,10,3,'products/1.jpg',50,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Refrigerador','Refrigerador no frost top freezer 340 litros',299990,10,3,'products/1.jpg',50,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Microondas','Microondas 17 litros digital',54990,10,3,'products/1.jpg',50,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cuchillos','Set de 4 cuchillos blade + soporte iman',10890,10,3,'products/1.jpg',48,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Tabla','Tabla para picar madera 20x30 cm café',4990,10,3,'products/1.jpg',48,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cucharon','Cuchara de silicona roja',2790,10,3,'products/1.jpg',48,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Rallador','Rallador multipropósito latón',3390,10,3,'products/1.jpg',48,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Encendedor','Encendedor cocina tubo grande',3990,10,3,'products/1.jpg',48,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Pesa','Pesa Digital de Cocina',3990,10,3,'products/1.jpg',48,101,5);
-- JARDIN
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cortacesped','Cortacésped a gasolina 46 cm 140 cc 5 HP',229990,10,3,'products/1.jpg',54,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Orillador','Orilladora eléctrica 350 W',25990,10,3,'products/1.jpg',54,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cortasetos','Cortasetos eléctrico 22" 600 W',59990,10,3,'products/1.jpg',54,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cosechador de olivos','Cosechador de olivos a gasolina 2,3 HP 52 cc',1590990,10,3,'products/1.jpg',54,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Inserticida','Insecticida natural para jardín 500 ml líquido',7190,10,3,'products/1.jpg',60,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Manguera','Set de manguera 18 m verde',13990,10,3,'products/1.jpg',63,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Gaoteros','Set de goteros botón regulables plástico 5 unidades',1190,10,3,'products/1.jpg',63,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Abono','Tierra con abono para jardín 35 litros saco',3250,10,3,'products/1.jpg',62,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Boega','Bodega jardín 192x134x204 cm',399990,10,3,'products/1.jpg',64,100,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Organizador','Organizador de jardín 90x39x68 cm Stilo Low',39990,10,3,'products/1.jpg',59,100,5);
-- FERRETERIA
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Caja Fuerte','Caja fuerte digital 17x20,5x17 cm blanco',24990,10,3,'products/1.jpg',68,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cerradura Pomo','Cerradura pomo acero antimicrobiana simple paso',5870,10,3,'products/1.jpg',65,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cerradura manillas','Cerradura acceso 9380 derecha inoxidable',25990,10,3,'products/1.jpg',65,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cerradura sobreponer','Cerradura sobreponer RIM 321BL',15290,10,3,'products/1.jpg',65,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cerradura sobreponer','Cerradura sobreponer RIM 321BL',15290,10,3,'products/1.jpg',65,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Alambre','Alambre de cobre aislado (H07V-U) 1,5 mm2 10 m Blanco',1470,10,3,'products/1.jpg',70,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cordon','Cordón 2x0,75 mm 10 m  Negro',4990,10,3,'products/1.jpg',70,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Radio','Radio Auto 2 Din +camara Retroceso+comando Volante',59990,10,3,'products/1.jpg',73,101,5);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Parlante','Parlante 10cm 4 vias potencia 320w',16990,10,3,'products/1.jpg',73,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Organizador auto','Organizador de carga 45 kg 19x47x14 cm PVC naranjo',11490,10,3,'products/1.jpg',73,101,1);
-- Pintura
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Adhesivo','Adhesivo de montaje agarre inmediato 100 ml',4190,10,3,'products/1.jpg',80,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cola Fria','Cola fría maderas 1 kg',6190,10,3,'products/1.jpg',80,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Brocha','Brocha multipropósito 2"',2390,10,3,'products/1.jpg',82,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Pistola pintar','Pistola para pintar control spray 100',69990,10,3,'products/1.jpg',82,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Rodillo','Rodrillo anti-goteo 23 cm',4490,10,3,'products/1.jpg',82,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cinta','Cinta para enmascarar 48 mm 40 m',2290,10,3,'products/1.jpg',82,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Esmalte','Esmalte Sintetico Cereluxe Aquatech Negro 1/4gl',8740,10,3,'products/1.jpg',86,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Pintura','Pintura látex habitacional blanco 1/4 gl',5140,10,3,'products/1.jpg',85,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Laca','Laca para madera 1 gl',23690,10,3,'products/1.jpg',88,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Preservante','Preservante de madera satinado 1 gl',22990,10,3,'products/1.jpg',88,100,1);
-- DECORACION
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Lampara colgar','Lámpara de colgar tela 1 luz E27 gris',11490,10,3,'products/1.jpg',90,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Led techo','Apliqué led techo dirigible 1 luz aluminio 10 W blanco',16990,10,3,'products/1.jpg',90,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Reloj','Reloj pared pajaros de chile',24990,10,3,'products/1.jpg',91,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Figura dedcorativa','Figura decorativa perro galgo cerámica 26 cm blanco',23990,10,3,'products/1.jpg',97,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Bonsai','Bonsai 23 cm hoja boj',7990,10,3,'products/1.jpg',97,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Campana viento','Campana de viento campanas metal',8790,10,3,'products/1.jpg',97,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Portavelas','Set de portavelas 2 unidades negro',12190,10,3,'products/1.jpg',97,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Vela','Vela decorativa 7x10 cm crema',4590,10,3,'products/1.jpg',97,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Mesa de centro','Mesa de centro 120x60x45 cm café',115990,10,3,'products/1.jpg',97,101,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('buda deco','Buda decorativo 19,5x14x8 cm poliresina plateado',6490,10,3,'products/1.jpg',97,101,1);
-- Mobiliario y ordenacion
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Cama americana','Cama americana excellence 1 plaza',114990,10,3,'products/1.jpg',107,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Sofa','Sofá 2 cuerpo tela 73x145x71 cm',119990,10,3,'products/1.jpg',103,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Sillon','Sillón de descanso reclinable negro',179990,10,3,'products/1.jpg',103,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Zapatero','Zapatero 7 repisas 67x30x138 cm Blanco',52990,10,3,'products/1.jpg',102,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Mesa','Mesa resina look madera 150x80 cm',69990,10,3,'products/1.jpg',100,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Silla','Silla cannes high 80x43x40 cm blancas',29990,10,3,'products/1.jpg',101,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Caja Organizadora','Caja organizadora 28 litros 42x32x31 cm transparente',3590,10,3,'products/1.jpg',104,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Sofa','Sofá 3 cuerpos connor marengo 188x77x76 cm',164990,10,3,'products/1.jpg',103,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Librero','Librero Essential wengue',109990,10,3,'products/1.jpg',98,100,1);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Closet','Clóset 4 puertas',84990,10,3,'products/1.jpg',99,100,1);
-- Climatizacion
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Aire acondicionado','Aire acondicionado Split inverter frío/calor 12.000 BTU AR12TSFZAWK/ZS',452990,10,3,'products/1.jpg',108,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Ventilador','Ventilador de pedestal 16',21990,10,3,'products/1.jpg',108,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Enfriador','Enfriador de aire 6 litros 65 W',49390,10,3,'products/1.jpg',113,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Deshumificador','Deshumidificador 15 litros 2200 W',237990,10,3,'products/1.jpg',113,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Purificador','Purificador de aire 39 m2',179990,10,3,'products/1.jpg',113,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Filtros','Filtro hepa purificador wurden',9990,10,3,'products/1.jpg',113,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Caja Sanitizador','Caja sanitizadora UV',99990,10,3,'products/1.jpg',113,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Termoventilador','Termoventilador eléctrico 1800 W',12990,10,3,'products/1.jpg',108,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Calefactor','Calefactor halógeno eléctrico',12990,10,3,'products/1.jpg',108,101,2);
INSERT INTO PRODUCTO(producto, descripcion, precio, stock, stock_critico, imagen_url, id_tipo_producto, id_proveedor, id_marca) VALUES ('Estufa','Estufa a gas 15 kg GH-42 RED',129990,10,3,'products/1.jpg',108,101,2);

commit;