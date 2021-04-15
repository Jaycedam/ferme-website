CREATE TABLE comuna (
    id_comuna     NUMBER NOT NULL,
    comuna        VARCHAR2(200) NOT NULL,
    id_provincia  NUMBER NOT NULL
);

ALTER TABLE comuna ADD CONSTRAINT comuna_pk PRIMARY KEY ( id_comuna );

CREATE TABLE domicilio (
    id_domicilio       NUMBER NOT NULL,
    calle              VARCHAR2(200) NOT NULL,
    nro                NUMBER NOT NULL,
    nro_departamento   NUMBER,
    id_comuna          NUMBER NOT NULL,
    id_tipo_domicilio  NUMBER NOT NULL,
    rut_persona        VARCHAR2(10) NOT NULL
);

ALTER TABLE domicilio ADD CONSTRAINT domicilio_pk PRIMARY KEY ( id_domicilio );

CREATE TABLE familia_producto (
    id_familia_producto  NUMBER NOT NULL,
    familia_producto     VARCHAR2(200) NOT NULL
);

ALTER TABLE familia_producto ADD CONSTRAINT familia_producto_pk PRIMARY KEY ( id_familia_producto );

CREATE TABLE nota_credito (
    nro_nota_credito  NUMBER NOT NULL,
    fecha             DATE NOT NULL,
    descripcion       VARCHAR2(500),
    nro_doc           NUMBER NOT NULL,
    rut_persona       VARCHAR2(10) NOT NULL
);

ALTER TABLE nota_credito ADD CONSTRAINT nota_credito_pk PRIMARY KEY ( nro_nota_credito );

CREATE TABLE nota_credito_detalle (
    id_detalle        NUMBER NOT NULL,
    cantidad          NUMBER NOT NULL,
    nro_nota_credito  NUMBER NOT NULL,
    id_producto       NUMBER NOT NULL
);

ALTER TABLE nota_credito_detalle ADD CONSTRAINT nota_credito_detalle_pk PRIMARY KEY ( id_detalle );

CREATE TABLE oc_detalle (
    id_oc_detalle    NUMBER NOT NULL,
    id_producto      NUMBER NOT NULL,
    cantidad         NUMBER NOT NULL,
    id_orden_compra  NUMBER NOT NULL
);

ALTER TABLE oc_detalle ADD CONSTRAINT oc_detalle_pk PRIMARY KEY ( id_oc_detalle );

CREATE TABLE orden_compra (
    id_orden_compra  NUMBER NOT NULL,
    total            NUMBER NOT NULL,
    id_proveedor     NUMBER NOT NULL
);

ALTER TABLE orden_compra ADD CONSTRAINT orden_compra_pk PRIMARY KEY ( id_orden_compra );

CREATE TABLE persona (
    rut_persona  VARCHAR2(10) NOT NULL,
    celular      NUMBER NOT NULL,
    usuario      NUMBER NOT NULL
);

ALTER TABLE persona ADD CONSTRAINT persona_pk PRIMARY KEY ( rut_persona );

CREATE TABLE producto (
    id_producto       NUMBER NOT NULL,
    producto          VARCHAR2(50) NOT NULL,
    descripcion       VARCHAR2(200),
    precio            NUMBER NOT NULL,
    stock             NUMBER NOT NULL,
    stock_critico     NUMBER NOT NULL,
    id_tipo_producto  NUMBER NOT NULL,
    id_proveedor      NUMBER NOT NULL
);

ALTER TABLE producto ADD CONSTRAINT producto_pk PRIMARY KEY ( id_producto );

CREATE TABLE proveedor (
    id_proveedor    NUMBER NOT NULL,
    nombre_empresa  VARCHAR2(200) NOT NULL,
    id_rubro        NUMBER NOT NULL,
    rut_persona     VARCHAR2(10) NOT NULL
);

CREATE UNIQUE INDEX proveedor__idx ON
    proveedor (
        rut_persona
    ASC );

ALTER TABLE proveedor ADD CONSTRAINT proveedor_pk PRIMARY KEY ( id_proveedor );

CREATE TABLE provincia (
    id_provincia  NUMBER NOT NULL,
    provincia     VARCHAR2(200) NOT NULL,
    id_region     NUMBER NOT NULL
);

ALTER TABLE provincia ADD CONSTRAINT provincia_pk PRIMARY KEY ( id_provincia );

CREATE TABLE recibo (
    nro_doc      NUMBER NOT NULL,
    fecha        DATE NOT NULL,
    subtotal     NUMBER NOT NULL,
    iva          NUMBER NOT NULL,
    total        NUMBER NOT NULL,
    id_tipo_doc  NUMBER NOT NULL,
    rut_persona  VARCHAR2(10) NOT NULL
);

ALTER TABLE recibo ADD CONSTRAINT recibo_pk PRIMARY KEY ( nro_doc );

CREATE TABLE recibo_detalle (
    id_detalle   NUMBER NOT NULL,
    id_producto  NUMBER NOT NULL,
    nro_doc      NUMBER NOT NULL,
    cantidad     NUMBER NOT NULL
);

ALTER TABLE recibo_detalle ADD CONSTRAINT recibo_detalle_pk PRIMARY KEY ( id_detalle );

CREATE TABLE region (
    id_region  NUMBER NOT NULL,
    region     VARCHAR2(200) NOT NULL
);

ALTER TABLE region ADD CONSTRAINT region_pk PRIMARY KEY ( id_region );

CREATE TABLE rubro (
    id_rubro  NUMBER NOT NULL,
    rubro     VARCHAR2(200) NOT NULL
);

ALTER TABLE rubro ADD CONSTRAINT rubro_pk PRIMARY KEY ( id_rubro );

CREATE TABLE tipo_documento (
    id_tipo_doc  NUMBER NOT NULL,
    tipo_doc     VARCHAR2(50) NOT NULL
);

ALTER TABLE tipo_documento ADD CONSTRAINT tipo_documento_pk PRIMARY KEY ( id_tipo_doc );

CREATE TABLE tipo_domicilio (
    id_tipo_domicilio  NUMBER NOT NULL,
    tipo_domicilio     VARCHAR2(50) NOT NULL
);

ALTER TABLE tipo_domicilio ADD CONSTRAINT tipo_domicilio_pk PRIMARY KEY ( id_tipo_domicilio );

CREATE TABLE tipo_producto (
    id_tipo_producto     NUMBER NOT NULL,
    tipo_producto        VARCHAR2(200) NOT NULL,
    id_familia_producto  NUMBER NOT NULL
);

ALTER TABLE tipo_producto ADD CONSTRAINT tipo_producto_pk PRIMARY KEY ( id_tipo_producto );

ALTER TABLE comuna
    ADD CONSTRAINT comuna_provincia_fk FOREIGN KEY ( id_provincia )
        REFERENCES provincia ( id_provincia );

ALTER TABLE domicilio
    ADD CONSTRAINT domicilio_comuna_fk FOREIGN KEY ( id_comuna )
        REFERENCES comuna ( id_comuna );

ALTER TABLE domicilio
    ADD CONSTRAINT domicilio_persona_fk FOREIGN KEY ( rut_persona )
        REFERENCES persona ( rut_persona );

ALTER TABLE domicilio
    ADD CONSTRAINT domicilio_tipo_fk FOREIGN KEY ( id_tipo_domicilio )
        REFERENCES tipo_domicilio ( id_tipo_domicilio );

ALTER TABLE nota_credito_detalle
    ADD CONSTRAINT nc_detalle_nota_credito_fk FOREIGN KEY ( nro_nota_credito )
        REFERENCES nota_credito ( nro_nota_credito );

ALTER TABLE nota_credito_detalle
    ADD CONSTRAINT nc_detalle_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE nota_credito
    ADD CONSTRAINT nota_credito_persona_fk FOREIGN KEY ( rut_persona )
        REFERENCES persona ( rut_persona );

ALTER TABLE nota_credito
    ADD CONSTRAINT nota_credito_recibo_fk FOREIGN KEY ( nro_doc )
        REFERENCES recibo ( nro_doc );

ALTER TABLE oc_detalle
    ADD CONSTRAINT oc_detalle_oc_fk FOREIGN KEY ( id_orden_compra )
        REFERENCES orden_compra ( id_orden_compra );

ALTER TABLE oc_detalle
    ADD CONSTRAINT oc_detalle_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE orden_compra
    ADD CONSTRAINT orden_compra_proveedor_fk FOREIGN KEY ( id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE producto
    ADD CONSTRAINT producto_proveedor_fk FOREIGN KEY ( id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE producto
    ADD CONSTRAINT producto_tipo_fk FOREIGN KEY ( id_tipo_producto )
        REFERENCES tipo_producto ( id_tipo_producto );

ALTER TABLE proveedor
    ADD CONSTRAINT proveedor_persona_fk FOREIGN KEY ( rut_persona )
        REFERENCES persona ( rut_persona );

ALTER TABLE proveedor
    ADD CONSTRAINT proveedor_rubro_fk FOREIGN KEY ( id_rubro )
        REFERENCES rubro ( id_rubro );

ALTER TABLE provincia
    ADD CONSTRAINT provincia_region_fk FOREIGN KEY ( id_region )
        REFERENCES region ( id_region );

ALTER TABLE recibo_detalle
    ADD CONSTRAINT recibo_detalle_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE recibo_detalle
    ADD CONSTRAINT recibo_detalle_recibo_fk FOREIGN KEY ( nro_doc )
        REFERENCES recibo ( nro_doc );

ALTER TABLE recibo
    ADD CONSTRAINT recibo_persona_fk FOREIGN KEY ( rut_persona )
        REFERENCES persona ( rut_persona );

ALTER TABLE recibo
    ADD CONSTRAINT recibo_tipo_fk FOREIGN KEY ( id_tipo_doc )
        REFERENCES tipo_documento ( id_tipo_doc );

ALTER TABLE tipo_producto
    ADD CONSTRAINT tipo_producto_familia_fk FOREIGN KEY ( id_familia_producto )
        REFERENCES familia_producto ( id_familia_producto );



