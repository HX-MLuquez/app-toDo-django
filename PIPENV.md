# 📦 Pipenv: El gestor de entornos virtuales y dependencias para Python

## 🔎 Cómo saber si tenés pipenv instalado

En la terminal ejecutá:

```bash
pipenv --version
```

Si está instalado, vas a ver algo como:

```
pipenv, version 2023.x.x
```

Si no está instalado, te va a decir algo como:

```
command not found
```

o

```
pipenv no se reconoce como comando interno o externo
```

---

## 📦 Cómo instalar pipenv

### Opción recomendada (instalarlo globalmente)

```bash
pip install pipenv
```

Después verificás:

```bash
pipenv --version
```

---

## ⚠️ Si el comando no funciona después de instalar

Puede ser que el ejecutable no esté en el PATH.
En Windows suele instalarse en:

```
C:\Users\TU_USUARIO\AppData\Roaming\Python\Python312\Scripts
```

Si pasa eso, podés probar:

```bash
python -m pipenv --version
```

Si eso funciona, entonces está instalado pero no agregado al PATH.

---

## Recomendación práctica

Como ya estás usando entornos virtuales y Django, instalarlo globalmente está bien. Pipenv se usa como herramienta de sistema, no dentro del entorno virtual.

---

Si querés, puedo explicarte también cuándo conviene pipenv vs venv vs poetry (ahí ya entramos en terreno más de desarrollador).
