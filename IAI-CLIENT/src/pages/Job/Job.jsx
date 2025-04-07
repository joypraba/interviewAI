import React, { useState, useMemo, useEffect } from "react";
import DataTable from "react-data-table-component";
import { FaEdit, FaTrash, FaUsers, FaPlus } from "react-icons/fa";
import { Link } from "react-router-dom";
import {getJobs} from "../../services/JobPosting"

const columns = [
  {
    id: 1,
    name: "Title",
    selector: (row) => row.title,
    sortable: true,
    reorder: true,
  },
  {
    id: 2,
    name: "Skills",
    selector: (row) => row.skills,
    sortable: true,
    reorder: true,
  },
  {
    id: 3,
    name: "Start Date",
    selector: (row) => row.startDate,
    sortable: true,
    right: true,
    reorder: true,
  },
  {
    id: 3,
    name: "End Date",
    selector: (row) => row.endDate,
    sortable: true,
    right: true,
    reorder: true,
  },
  {
    name: "Actions",
    cell: row => (
      <div className="d-flex gap-2">
        <button
          className="btn btn-sm btn-primary"
          onClick={() => handleEdit(row)}
          title="Edit"
        >
          <FaEdit />
        </button>
        
      </div>
    ),
    ignoreRowClick: true,
    allowOverflow: true,
    button: true,
  },
];

const Jobs = () => {
  const [filterText, setFilterText] = useState("");
  const [jobs, setJobs] = useState([]);
  const [resetPaginationToggle, setResetPaginationToggle] = React.useState(false);
  


  const handleEdit = (row) => {
    console.log("Edit", row);
    // Navigate or open modal
  };

  
  
  const filteredItems = jobs?.filter(item => item.title && item.title.toLowerCase().includes(filterText.toLowerCase()));
  const subHeaderComponentMemo = React.useMemo(() => {
    const handleClear = () => {
      if (filterText) {
        setResetPaginationToggle(!resetPaginationToggle);
        setFilterText('');
      }
    };
    return <div className="d-flex justify-content-between align-items-center w-100 "><input
      type="text"
      placeholder="Search by title"
      className="form-control w-25"
      value={filterText}
      onChange={e => setFilterText(e.target.value)}
    />
      <Link to="/admin/jobs/add">
        <button className="btn btn-success" >
          <FaPlus className="me-1" /> Add Job
        </button>
      </Link> </div >;
  }, [filterText, resetPaginationToggle]);

  useEffect(() => {
      const fetchJobs = async () => {
        try {
          const jobData = await getJobs();
          if (jobData?.data) {
            setJobs(jobData.data);
          }
        } catch (error) {
          console.error("Failed to fetch candidates", error);
        }
      };
  
      fetchJobs();
    }, []);

  return (
    <DataTable
      title="Jobs"
      columns={columns}
      data={filteredItems}
      defaultSortFieldId={1}
      pagination
      subHeader
      subHeaderComponent={subHeaderComponentMemo}
      selectableRows
    />
  )
}


export default Jobs;