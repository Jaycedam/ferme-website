-- Generated by Oracle SQL Developer Data Modeler 21.1.0.092.1221
--   at:        2021-06-08 18:57:03 CLT
--   site:      Oracle Database 11g
--   type:      Oracle Database 11g



-- predefined type, no DDL - MDSYS.SDO_GEOMETRY

-- predefined type, no DDL - XMLTYPE

CREATE TABLE comuna (
    id_comuna     NUMBER NOT NULL,
    comuna        VARCHAR2(200) NOT NULL,
    id_provincia  NUMBER NOT NULL
);

ALTER TABLE comuna ADD CONSTRAINT comuna_pk PRIMARY KEY ( id_comuna );

CREATE TABLE domicilio (
    id_domicilio      NUMBER NOT NULL,
    calle             VARCHAR2(200) NOT NULL,
    nro               NUMBER NOT NULL,
    nro_departamento  NUMBER,
    id_comuna         NUMBER NOT NULL,
    rut_persona       VARCHAR2(10) NOT NULL
);

CREATE UNIQUE INDEX domicilio__idx ON
    domicilio (
        rut_persona
    ASC );

ALTER TABLE domicilio ADD CONSTRAINT domicilio_pk PRIMARY KEY ( id_domicilio );

CREATE TABLE estado (
    id_estado  NUMBER NOT NULL,
    estado     VARCHAR2(50) NOT NULL
);

ALTER TABLE estado ADD CONSTRAINT estado_pk PRIMARY KEY ( id_estado );

CREATE TABLE familia_producto (
    id_familia_producto  NUMBER NOT NULL,
    familia_producto     VARCHAR2(200) NOT NULL,
    imagen_url           VARCHAR2(500)
);

ALTER TABLE familia_producto ADD CONSTRAINT familia_producto_pk PRIMARY KEY ( id_familia_producto );

CREATE TABLE marca (
    id_marca  NUMBER NOT NULL,
    marca     VARCHAR2(200) NOT NULL
);

ALTER TABLE marca ADD CONSTRAINT marca_pk PRIMARY KEY ( id_marca );

CREATE TABLE orden (
    nro_orden     NUMBER NOT NULL,
    fecha         DATE NOT NULL,
    total         NUMBER NOT NULL,
    rut_persona   VARCHAR2(10) NOT NULL,
    id_tipo       NUMBER NOT NULL,
    id_proveedor  NUMBER,
    id_estado     NUMBER NOT NULL
);

ALTER TABLE orden ADD CONSTRAINT orden_pk PRIMARY KEY ( nro_orden );

CREATE TABLE orden_detalle (
    id_detalle   NUMBER NOT NULL,
    id_producto  NUMBER NOT NULL,
    precio       NUMBER NOT NULL,
    cantidad     NUMBER NOT NULL,
    total        NUMBER NOT NULL,
    nro_orden    NUMBER NOT NULL
);

ALTER TABLE orden_detalle ADD CONSTRAINT orden_detalle_pk PRIMARY KEY ( id_detalle );

CREATE TABLE persona (
    rut_persona  VARCHAR2(10) NOT NULL,
    celular      NUMBER NOT NULL,
    usuario      NUMBER NOT NULL
);

ALTER TABLE persona ADD CONSTRAINT persona_pk PRIMARY KEY ( rut_persona );

CREATE TABLE producto (
    id_producto        NUMBER NOT NULL,
    producto           VARCHAR2(50) NOT NULL,
    descripcion        VARCHAR2(200),
    precio             NUMBER NOT NULL,
    precio_proveedor   NUMBER NOT NULL,
    stock              NUMBER NOT NULL,
    stock_critico      NUMBER NOT NULL,
    imagen_url         VARCHAR2(500),
    fecha_vencimiento  DATE,
    id_tipo_producto   NUMBER NOT NULL,
    id_proveedor       NUMBER NOT NULL,
    id_marca           NUMBER NOT NULL
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
    nro_recibo  NUMBER NOT NULL,
    fecha       DATE NOT NULL,
    subtotal    NUMBER NOT NULL,
    iva         NUMBER NOT NULL,
    total       NUMBER NOT NULL,
    id_tipo     NUMBER NOT NULL,
    nro_orden   NUMBER NOT NULL
);

CREATE UNIQUE INDEX recibo__idx ON
    recibo (
        nro_orden
    ASC );

ALTER TABLE recibo ADD CONSTRAINT recibo_pk PRIMARY KEY ( nro_recibo );

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
    id_tipo         NUMBER NOT NULL,
    tipo_documento  VARCHAR2(200) NOT NULL
);

ALTER TABLE tipo_documento ADD CONSTRAINT tipo_documento_pk PRIMARY KEY ( id_tipo );

CREATE TABLE tipo_orden (
    id_tipo  NUMBER NOT NULL,
    tipo     VARCHAR2(50) NOT NULL
);

ALTER TABLE tipo_orden ADD CONSTRAINT tipo_orden_pk PRIMARY KEY ( id_tipo );

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

ALTER TABLE orden_detalle
    ADD CONSTRAINT orden_detalle_orden_fk FOREIGN KEY ( nro_orden )
        REFERENCES orden ( nro_orden );

ALTER TABLE orden_detalle
    ADD CONSTRAINT orden_detalle_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE orden
    ADD CONSTRAINT orden_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado ( id_estado );

ALTER TABLE orden
    ADD CONSTRAINT orden_persona_fk FOREIGN KEY ( rut_persona )
        REFERENCES persona ( rut_persona );

ALTER TABLE orden
    ADD CONSTRAINT orden_proveedor_fk FOREIGN KEY ( id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE orden
    ADD CONSTRAINT orden_tipo_fk FOREIGN KEY ( id_tipo )
        REFERENCES tipo_orden ( id_tipo );

ALTER TABLE producto
    ADD CONSTRAINT producto_marca_fk FOREIGN KEY ( id_marca )
        REFERENCES marca ( id_marca );

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

ALTER TABLE recibo
    ADD CONSTRAINT recibo_orden_fk FOREIGN KEY ( nro_orden )
        REFERENCES orden ( nro_orden );

ALTER TABLE recibo
    ADD CONSTRAINT recibo_tipo_fk FOREIGN KEY ( id_tipo )
        REFERENCES tipo_documento ( id_tipo );

ALTER TABLE tipo_producto
    ADD CONSTRAINT tipo_producto_familia_fk FOREIGN KEY ( id_familia_producto )
        REFERENCES familia_producto ( id_familia_producto );



-- Oracle SQL Developer Data Modeler Summary Report: 
-- 
-- CREATE TABLE                            17
-- CREATE INDEX                             3
-- ALTER TABLE                             35
-- CREATE VIEW                              0
-- ALTER VIEW                               0
-- CREATE PACKAGE                           0
-- CREATE PACKAGE BODY                      0
-- CREATE PROCEDURE                         0
-- CREATE FUNCTION                          0
-- CREATE TRIGGER                           0
-- ALTER TRIGGER                            0
-- CREATE COLLECTION TYPE                   0
-- CREATE STRUCTURED TYPE                   0
-- CREATE STRUCTURED TYPE BODY              0
-- CREATE CLUSTER                           0
-- CREATE CONTEXT                           0
-- CREATE DATABASE                          0
-- CREATE DIMENSION                         0
-- CREATE DIRECTORY                         0
-- CREATE DISK GROUP                        0
-- CREATE ROLE                              0
-- CREATE ROLLBACK SEGMENT                  0
-- CREATE SEQUENCE                          0
-- CREATE MATERIALIZED VIEW                 0
-- CREATE MATERIALIZED VIEW LOG             0
-- CREATE SYNONYM                           0
-- CREATE TABLESPACE                        0
-- CREATE USER                              0
-- 
-- DROP TABLESPACE                          0
-- DROP DATABASE                            0
-- 
-- REDACTION POLICY                         0
-- 
-- ORDS DROP SCHEMA                         0
-- ORDS ENABLE SCHEMA                       0
-- ORDS ENABLE OBJECT                       0
-- 
-- ERRORS                                   0
-- WARNINGS                                 0
