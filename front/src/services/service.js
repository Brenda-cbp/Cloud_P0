import React from 'react';
import { saveToken, getToken } from './auth';

const token = getToken(); // Obtiene el token de localStorage

const back = "http://127.0.0.1:8000"
const login = async (username, password) => {
    try {
        const response = await fetch(back + '/usuarios/iniciar-sesion', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre_usuario: username,
                contrasenia: password
            })
        });
        if (!response.ok) {
            throw new Error('Error al iniciar sesión');
        }

        const data = await response.json();
        saveToken(data.access_token);
        return data; // Retorna los datos del usuario si la solicitud fue exitosa
    } catch (error) {
        throw new Error('Error al iniciar sesión:', error);
    }
};

const signUp = async (username, password, image) => {
    try {
        const response = await fetch(back + '/usuarios', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                nombre_usuario: username,
                contrasenia: password,
                imagen_perfil: image
            })
        });
        const data = await response.json();
        return data;
    } catch (error) {
        throw new Error('Error al iniciar sesión:', error);
    }
};
// ---------------------------------------------------------------------------
// C A T E G O R I A 
// ---------------------------------------------------------------------------

const postCategoria = async (name, description) => {
    try {
        const response = await fetch(back + '/categorias', {
            mode: 'cors',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getToken()}`
            },
            body: JSON.stringify({
                nombre: name,
                descripcion: description
            })
        });
        const data = await response.json();
        return data;
    } catch (error) {
        throw new Error('Error al crear Categoria:', error);
    }
};

const getCategorias = async () => {
    try {
        const response = await fetch(`${back}/categorias`, {
            mode: 'cors',
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getToken()}`
            }
        });
        const data = await response.json();
        return data;
    } catch (error) {
        throw new Error('Error al obtener categorías:', error);
    }
};

const deleteCategoria = async (categoriaId) => {
    try {
        const response = await fetch(`${back}/categorias/${categoriaId}`, {
            mode: 'cors',
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getToken()}`
            }
        });
        const data = await response.json();
        return data;

    } catch (error) {
        throw new Error('Error en la solicitud de eliminación de categoría:', error);
    }
};


// ---------------------------------------------------------------------------
// T A R E A
// ---------------------------------------------------------------------------

const createTask = async (taskData) => {
    try {
        const response = await fetch(back + '/tareas', {
            mode: 'cors',
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getToken()}`
            },
            body: JSON.stringify(taskData)
        });

        if (!response.ok) {
            throw new Error('Error al crear la tarea');
        }
        const data = await response.json();
        return data;
    } catch (error) {
        throw new Error('Error en la solicitud de creación de tarea:', error);
    }
};


const getTareasByUser = async (id) => {
    try {
        const response = await fetch(`${back}/tareas/usuario/${id}`, {
            mode: 'cors',
            method: 'GET',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getToken()}`
            }
        });
        const data = await response.json();
        console.log(data)
        return data;
    } catch (error) {
        throw new Error('Error al obtener las tareas:', error);
    }
}

const deleteTarea = async (tareaId) => {
    try {
        const response = await fetch(`${back}/tareas/${tareaId}`, {
            mode: 'cors',
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json',
                'Authorization': `Bearer ${getToken()}`
            }
        });
        const data = await response.json();
        return data;

    } catch (error) {
        throw new Error('Error en la solicitud de eliminación de la tarea:', error);
    }
};
export { login, signUp, postCategoria, getCategorias, createTask, getTareasByUser, deleteCategoria, deleteTarea };
