# security-test-client-python

La prueba de seguridad es un servicio "echo" que se encargará de verificar que el mensaje y la firma correspondan a tu aplicación; asimismo retornará el mismo mensaje con nuestra respectiva firma, que también deberás verificar.

## Requisitos

1. Python >= 3.9

## Guía de inicio

### Paso 1. Generar llave y certificado

Antes de lanzar la prueba se deberá tener un keystore para la llave privada y el certificado asociado a ésta.
Para generar el keystore se ejecutan las instrucciones que se encuentran en ***/createKeystore.sh***

### Paso 2. Carga del certificado dentro del portal de desarrolladores
 1. Iniciar sesión.
 2. Dar clic en la sección "**Mis aplicaciones**".
 3. Seleccionar la aplicación.
 4. Ir a la pestaña de "**Certificados para @tuApp**".
    <p align="center">
      <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/applications.png">
    </p>
 5. Al abrirse la ventana emergente, seleccionar el certificado previamente creado y dar clic en el botón "**Cargar**":
    <p align="center">
      <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/upload_cert.png" width="268">
    </p>

### Paso 3. Descarga del certificado de Círculo de Crédito dentro del portal de desarrolladores
 1. Iniciar sesión.
 2. Dar clic en la sección "**Mis aplicaciones**".
 3. Seleccionar la aplicación.
 4. Ir a la pestaña de "**Certificados para @tuApp**".
    <p align="center">
        <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/applications.png">
    </p>
 5. Al abrirse la ventana emergente, dar clic al botón "**Descargar**":
    <p align="center">
        <img src="https://github.com/APIHub-CdC/imagenes-cdc/blob/master/download_cert.png" width="268">
    </p>

### Paso 4. Modificar archivo de configuraciones

Para hacer uso del certificado que se descargó y el keystore que se creó se deberán modificar las rutas que se encuentran en ***/test.py***

```python
def unit_test(self):
    	x_api_key = "your_x_api_key"
    	password = "your_keystore_password"
    	pathKeypair = "/your_path/keypair.p12"
    	pathCertificateCdc = "/your_path/cdc_cert.pem"
```

### Paso 5. Modificar URL

Modificar la URL de la petición en ***/test.py*** en la línea 12, como se muestra en el siguiente fragmento de código:

```python
basePath = "the_url"
```

### Paso 6. Capturar los datos de la petición

En el archivo **/test.py**, se deberá modificar el siguiente fragmento de código con los datos correspondientes:

```python
x_api_key = "your_x_api_key"
password = "your_keystore_password"
pathKeypair = "/your_path/keypair.p12"
pathCertificateCdc = "/your_path/cdc_cert.pem"
```

### Paso 7. Ejecutar la prueba unitaria

Teniendo los pasos anteriores ya solo falta ejecutar la prueba unitaria, con el siguiente comando:

```shell
python3 test.py
```