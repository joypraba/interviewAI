import React from "react";
import { Link } from "react-router-dom";
const Sidebar = () => {

    return (
        <nav id="sidebar" className="sidebar js-sidebar">
            <div className="sidebar-content js-simplebar">
                <a className="sidebar-brand" href="index.html">
                    <span className="align-middle">Interview AI</span>
                </a>

                <ul className="sidebar-nav">
                    <li className="sidebar-header">Pages</li>

                    <li className="sidebar-item active">
                        <Link className="sidebar-link" to="/admin/jobs">
                            <i className="align-middle" data-feather="sliders"></i>
                            <span className="align-middle">Job Posting</span>
                        </Link>
                    </li>

                    <li className="sidebar-item">
                        <Link className="sidebar-link" to="/admin/candidates">
                            <i className="align-middle" data-feather="user"></i>
                            <span className="align-middle">Candidates</span>
                        </Link>
                    </li>
                    <li className="sidebar-item">
                        <Link className="sidebar-link" to="/admin/applications">
                            <i className="align-middle" data-feather="user"></i>
                            <span className="align-middle">Applications</span>
                        </Link>
                    </li>

                    <li className="sidebar-item">
                        <Link className="sidebar-link" to="/admin/applications">
                            <i className="align-middle" data-feather="user"></i>
                            <span className="align-middle">Jobs</span>
                        </Link>
                    </li>
                    <li className="sidebar-item">
                        <Link className="sidebar-link" to="/admin/appliedJobs">
                            <i className="align-middle" data-feather="user"></i>
                            <span className="align-middle">Applied Jobs</span>
                        </Link>
                    </li>
                </ul>
            </div>
        </nav>

    )
}


export default Sidebar;