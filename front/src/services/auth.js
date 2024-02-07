// auth.js

const TOKEN_KEY = 'token';
const USERNAME_KEY = 'username';
const USER_IMAGE_KEY = 'userImage';

// Guardar el token, nombre de usuario y imagen en localStorage
export const saveAuthData = (token, username, userImage) => {
  localStorage.setItem(TOKEN_KEY, token);
  localStorage.setItem(USERNAME_KEY, username);
  localStorage.setItem(USER_IMAGE_KEY, userImage);
};

// Obtener el token desde localStorage
export const getToken = () => {
  return localStorage.getItem(TOKEN_KEY);
};

// Obtener el nombre de usuario desde localStorage
export const getUsername = () => {
  return localStorage.getItem(USERNAME_KEY);
};

// Obtener la imagen del usuario desde localStorage
export const getUserImage = () => {
  return localStorage.getItem(USER_IMAGE_KEY);
};

// Eliminar el token, nombre de usuario y imagen de localStorage
export const removeAuthData = () => {
  localStorage.removeItem(TOKEN_KEY);
  localStorage.removeItem(USERNAME_KEY);
  localStorage.removeItem(USER_IMAGE_KEY);
};
