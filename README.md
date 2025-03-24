# Transferencia de Archivos con AWS Lambda - AWSome Women Summit - Tercera Edicion

Este proyecto demuestra cómo transferir archivos desde **Azure ADLS Gen2 hacia AWS S3** utilizando **AWS Lambda**.

Fue creado para el evento **AWSome Women CS25** como una demo práctica de integración entre nubes usando arquitectura serverless.

---

## 📌 Objetivo

Automatizar la transferencia de archivos entre Azure y AWS utilizando:
- SDK de Azure Blob Storage
- AWS Lambda y Boto3
- Acceso IAM entre nubes

---

## 📁 Archivos Incluidos

- `LambdaSourceCode-FromAzureADLS2AWSS3.py`: Función Lambda principal que realiza la transferencia.
- `README.md`: Este archivo de documentación.
- `AWSome Women CS25 - YAA`: Presentación utilizada durante el evento.

---

## ▶️ Demo en Video

Mira la demostración completa en YouTube:

[![YouTube Demo](https://img.youtube.com/vi/YZ4rMVHqX1s/0.jpg)](https://www.youtube.com/watch?v=YZ4rMVHqX1s)

👉 [Haz clic aquí para ver el video](https://www.youtube.com/watch?v=YZ4rMVHqX1s)

---

## 🚀 ¿Cómo usar?

1. Despliega el código de la función Lambda en tu cuenta de AWS.
2. Configura las variables de entorno con las credenciales de almacenamiento de Azure.
3. Ejecuta la función para probar la transferencia desde ADLS Gen2 hacia S3.
