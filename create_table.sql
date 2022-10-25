CREATE TABLE public.measurer_data (
    mac_name character varying(255) NOT NULL,
    datetime DATE NOT NULL,
    rssi boolean NOT NULL,
    va integer NOT NULL, 
    vb integer NOT NULL,
    vc integer NOT NULL,
    ia integer NOT NULL,
    ib integer NOT NULL,
    ic integer NOT NULL,
    wa integer NOT NULL,
    wb integer NOT NULL,
    wc integer NOT NULL
);

ALTER TABLE ONLY public.measurer_data
    ADD CONSTRAINT PK_measurer_data PRIMARY KEY (mac_name);