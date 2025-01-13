CREATE TABLE delivery (
    id_delivery       NUMBER NOT NULL,
    nro_orden         NUMBER NOT NULL,
    calle             VARCHAR2(200) NOT NULL,
    nro               NUMBER NOT NULL,
    nro_departamento  NUMBER
);

CREATE UNIQUE INDEX delivery__idx ON
    delivery (
        nro_orden
    ASC );

ALTER TABLE delivery ADD CONSTRAINT delivery_pk PRIMARY KEY ( id_delivery );

CREATE TABLE domicilio (
    id_domicilio      NUMBER NOT NULL,
    calle             VARCHAR2(200) NOT NULL,
    nro               NUMBER NOT NULL,
    nro_departamento  NUMBER,
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

CREATE TABLE motivo (
    id_motivo  NUMBER NOT NULL,
    motivo     VARCHAR2(200) NOT NULL
);

ALTER TABLE motivo ADD CONSTRAINT motivo_pk PRIMARY KEY ( id_motivo );

CREATE TABLE nc_detalle (
    id_detalle        NUMBER NOT NULL,
    id_producto       NUMBER NOT NULL,
    precio            NUMBER NOT NULL,
    cantidad          NUMBER NOT NULL,
    total             NUMBER NOT NULL,
    nro_nota_credito  NUMBER NOT NULL
);

ALTER TABLE nc_detalle ADD CONSTRAINT nc_detalle_pk PRIMARY KEY ( id_detalle );

CREATE TABLE nota_credito (
    nro_nota_credito  NUMBER NOT NULL,
    fecha             DATE NOT NULL,
    total             NUMBER NOT NULL,
    descripcion       VARCHAR2(500),
    id_estado         NUMBER NOT NULL,
    id_motivo         NUMBER NOT NULL,
    nro_orden         NUMBER NOT NULL
);

ALTER TABLE nota_credito ADD CONSTRAINT nota_credito_pk PRIMARY KEY ( nro_nota_credito );

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
    nro_orden    NUMBER NOT NULL,
    id_producto  NUMBER NOT NULL,
    precio       NUMBER NOT NULL,
    cantidad     NUMBER NOT NULL,
    total        NUMBER NOT NULL
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

ALTER TABLE delivery
    ADD CONSTRAINT delivery_orden_fk FOREIGN KEY ( nro_orden )
        REFERENCES orden ( nro_orden );

ALTER TABLE domicilio
    ADD CONSTRAINT domicilio_persona_fk FOREIGN KEY ( rut_persona )
        REFERENCES persona ( rut_persona );

ALTER TABLE nc_detalle
    ADD CONSTRAINT nc_detalle_nota_credito_fk FOREIGN KEY ( nro_nota_credito )
        REFERENCES nota_credito ( nro_nota_credito );

ALTER TABLE nc_detalle
    ADD CONSTRAINT nc_detalle_producto_fk FOREIGN KEY ( id_producto )
        REFERENCES producto ( id_producto );

ALTER TABLE nota_credito
    ADD CONSTRAINT nota_credito_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado ( id_estado );

ALTER TABLE nota_credito
    ADD CONSTRAINT nota_credito_motivo_fk FOREIGN KEY ( id_motivo )
        REFERENCES motivo ( id_motivo );

ALTER TABLE nota_credito
    ADD CONSTRAINT nota_credito_orden_fk FOREIGN KEY ( nro_orden )
        REFERENCES orden ( nro_orden );

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
    ADD CONSTRAINT orden_tipo_orden_fk FOREIGN KEY ( id_tipo )
        REFERENCES tipo_orden ( id_tipo );

ALTER TABLE producto
    ADD CONSTRAINT producto_marca_fk FOREIGN KEY ( id_marca )
        REFERENCES marca ( id_marca );

ALTER TABLE producto
    ADD CONSTRAINT producto_proveedor_fk FOREIGN KEY ( id_proveedor )
        REFERENCES proveedor ( id_proveedor );

ALTER TABLE producto
    ADD CONSTRAINT producto_tipo_producto_fk FOREIGN KEY ( id_tipo_producto )
        REFERENCES tipo_producto ( id_tipo_producto );

ALTER TABLE proveedor
    ADD CONSTRAINT proveedor_persona_fk FOREIGN KEY ( rut_persona )
        REFERENCES persona ( rut_persona );

ALTER TABLE proveedor
    ADD CONSTRAINT proveedor_rubro_fk FOREIGN KEY ( id_rubro )
        REFERENCES rubro ( id_rubro );

ALTER TABLE recibo
    ADD CONSTRAINT recibo_orden_fk FOREIGN KEY ( nro_orden )
        REFERENCES orden ( nro_orden );

ALTER TABLE recibo
    ADD CONSTRAINT recibo_tipo_documento_fk FOREIGN KEY ( id_tipo )
        REFERENCES tipo_documento ( id_tipo );

ALTER TABLE tipo_producto
    ADD CONSTRAINT tipo_producto_familia_fk FOREIGN KEY ( id_familia_producto )
        REFERENCES familia_producto ( id_familia_producto );
