
import React from "react";
import { getAccessData } from "../../utils/Auth";
import { useNavigate } from "react-router-dom";

const Navbar = () => {
    const navigate = useNavigate();
    const accessData = getAccessData()
    const logout = () => {
        sessionStorage.removeItem("acces_data");
        navigate("/");
    }

    return (
        <nav className="navbar navbar-expand navbar-light navbar-bg">
            <a className="sidebar-toggle js-sidebar-toggle" href="#!">
                <i className="hamburger align-self-center" />
            </a>

            <div className="navbar-collapse collapse">
                <ul className="navbar-nav navbar-align">
                {/* Notifications */}
                

                {/* User Profile */}
                <li className="nav-item dropdown">
                    <a className="nav-icon dropdown-toggle d-inline-block d-sm-none" href="#!" data-bs-toggle="dropdown">
                    <i className="align-middle" data-feather="settings" />
                    </a>
                    <a className="nav-link dropdown-toggle d-none d-sm-inline-block" href="#!" data-bs-toggle="dropdown">
                    <span className="text-dark">{accessData.name}</span>
                    </a>
                    <div className="dropdown-menu dropdown-menu-end">
                    {/* <a className="dropdown-item" href="pages-profile.html"><i className="align-middle me-1" data-feather="user" /> Profile</a>
                    <a className="dropdown-item" href="#!"><i className="align-middle me-1" data-feather="pie-chart" /> Analytics</a>
                    <div className="dropdown-divider" />
                    <a className="dropdown-item" href="index.html"><i className="align-middle me-1" data-feather="settings" /> Settings & Privacy</a>
                    <a className="dropdown-item" href="#!"><i className="align-middle me-1" data-feather="help-circle" /> Help Center</a>
                    <div className="dropdown-divider" /> */}
                    <a className="dropdown-item" href="#!" onClick={logout}>Log out</a>
                    </div>
                </li>
                </ul>
            </div>
            </nav>

    )
}


export default Navbar;