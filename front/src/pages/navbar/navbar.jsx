import React from 'react'
import { Container, Nav, Navbar, Button, Form } from 'react-bootstrap'
import { Link, useNavigate } from 'react-router-dom';
import "./navbar.css"

function NavBar(props) {
    const id = props.id;
    const navigate = useNavigate();
    return (
        <div >
            <Navbar expand="lg">
                <Container fluid>
                    <Navbar.Toggle aria-controls="navbarScroll" />
                    <Navbar.Collapse id="navbarScroll">
                        <Nav
                            className="me-auto my-2 my-lg-0"
                            style={{ maxHeight: '100px' }}
                            navbarScroll
                        >   <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/${id}/tareas`)}>Ver Tareas</Nav.Link>
                            <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/${id}/newTask`)}>Crear Tarea</Nav.Link>
                            <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/${id}/categorias`)}>Ver Categorias</Nav.Link>
                            <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/${id}/newCategoria`)}>Crear Categoria</Nav.Link>
                            <Nav.Link style={{ color: "white" }} onClick={() => navigate(`/`)}>Log Out</Nav.Link>
                            {/* <Nav.Link onClick={() => navigate(`/${id}/recomendaciones`)}>Mis recomendaciones</Nav.Link> */}
                        </Nav>
                       
                    </Navbar.Collapse>
                </Container>
            </Navbar>
            <hr />
        </div >

    );
}
export default NavBar