import React from 'react'
import { Container, Nav, Navbar, Button, Form } from 'react-bootstrap'
import { Link, useNavigate } from 'react-router-dom';
import "./navbar.css"
import { getUserImage, getUsername, removeAuthData } from '../../services/auth';

function NavBar(props) {
    const id = props.id;
    const username =  getUsername();
    const userImage = getUserImage();
    const navigate = useNavigate();
   
const handleLogout = () => {
    removeAuthData();
    navigate(`/`);
};
    return (
        <div>
            <Navbar expand="lg">
                <Container fluid>
                    <Navbar.Toggle aria-controls="navbarScroll" />
                    <Navbar.Collapse id="navbarScroll">
                        <Nav
                            className="me-auto my-2 my-lg-0"
                            style={{ maxHeight: '100px' }}
                            navbarScroll
                        >
                            <img src={userImage} alt="User" style={{ width: '40px', borderRadius: '50%', marginRight: '10px' }} />
                            <span style={{ color: 'white', marginRight: '10px' }}>{username}</span>
                            <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/${id}/tareas`)}>Ver Tareas</Nav.Link>
                            <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/${id}/newTask`)}>Crear Tarea</Nav.Link>
                            <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/${id}/categorias`)}>Ver Categorias</Nav.Link>
                            <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/${id}/newCategoria`)}>Crear Categoria</Nav.Link>
                            <Nav.Link style={{ color: "white" }} onClick={() => handleLogout()}>Log Out</Nav.Link>
                        </Nav>
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            <hr />
        </div>
    );
}
export default NavBar