import React, { useState } from "react";
import "./Job.css"
import CreatableSelect from 'react-select/creatable';
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

function AddJobs() {
    const [skills, setSkills] = useState([])
    const [startDate, setStartDate] = useState("")
    return (
        <main className="content">
            <div className="container-fluid p-0">
                <h1 className="h3 mb-3">Add Jobs</h1>
                <div className="row">
                    <div className="col-12">
                        <div className="card">
                            <div className="card-body">
                                <div className="row">
                                    <div className="col-12 d-flex">
                                        <div className=" col-6">
                                            <div className="card-header">
                                                <h5 className="card-title mb-0">Title</h5>
                                            </div>
                                            <div className="card-body">
                                                <input type="text" className="form-control" placeholder="Enter Title" />
                                            </div>
                                        </div>

                                        {/* Skills Card */}
                                        <div className=" col-6">
                                            <div className="card-header">
                                                <h5 className="card-title mb-0">Skills</h5>
                                            </div>
                                            <div className="card-body">
                                                <CreatableSelect
                                                    isMulti
                                                    onChange={(selectedOptions) => setSkills(selectedOptions)}
                                                    options={[]}
                                                    placeholder="Enter or create tags..."
                                                    value={skills}
                                                />
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-12 d-flex">
                                        <div className=" col-6">
                                            <div className="card-header">
                                                <h5 className="card-title mb-0">Description</h5>
                                            </div>
                                            <div className="card-body">
                                                <input type="text" className="form-control" placeholder="Enter Description" />
                                            </div>
                                        </div>
                                        <div className=" col-6">
                                            <div className="card-header">
                                                <h5 className="card-title mb-0">Start Date</h5>
                                            </div>
                                            <div className="card-body">
                                                <DatePicker className="form-control" selected={startDate} onChange={(date) => setStartDate(date)} />
                                            </div>
                                        </div>
                                    </div>
                                    <div className="col-12 d-flex">
                                        
                                        <div className=" col-6">
                                            <div className="card-header">
                                                <h5 className="card-title mb-0">End Date</h5>
                                            </div>
                                            <div className="card-body">
                                                <DatePicker className="form-control" selected={startDate} onChange={(date) => setStartDate(date)} />
                                            </div>
                                        </div>
                                        <div className=" col-6 align-self-center">
                                            <div className="card-body">
                                                <input type="button" className="btn btn-primary " value="Save" />
                                            </div>
                                        </div>
                                    </div>
                                </div>

                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </main>

    );
}

export default AddJobs;