import React, { useState, useMemo, useEffect } from "react";
import DataTable from "react-data-table-component";
import { FaEdit, FaTrash, FaUsers, FaPlus } from "react-icons/fa";
import { Link } from "react-router-dom";
import {getApplications} from "../../services/Application"

const columns = [
  {
    id: 1,
    name: "Name",
    selector: (row) => row.candidate.name,
    sortable: true,
    reorder: true,
  },
  {
    id: 2,
    name: "Email",
    selector: (row) => row.candidate.email,
    sortable: true,
    reorder: true,
  },
  {
    id: 3,
    name: "Job Title",
    selector: (row) => row.job.title,
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

const Candidate = () => {
  const [filterText, setFilterText] = useState("");
  const [applications, setApplications] = useState([]);
  const [resetPaginationToggle, setResetPaginationToggle] = React.useState(false);
  
  const handleAdd = () => {

  }

  const handleEdit = (row) => {
    console.log("Edit", row);
    // Navigate or open modal
  };
  
  const handleDelete = (row) => {
    if (window.confirm(`Are you sure you want to delete "${row.title}"?`)) {
      console.log("Deleted", row);
      // Call API or update state
    }
  };
  
  const handleAppliedCandidates = (row) => {
    console.log("View applied candidates for", row);
    // Redirect or show modal
  };
  
  
  const filteredItems = applications.filter(item => item.candidate.name && item.candidate.name.toLowerCase().includes(filterText.toLowerCase()));
  const subHeaderComponentMemo = React.useMemo(() => {
    const handleClear = () => {
      if (filterText) {
        setResetPaginationToggle(!resetPaginationToggle);
        setFilterText('');
      }
    };
    return <input
      type="text"
      placeholder="Search by title"
      className="form-control w-25"
      value={filterText}
      onChange={e => setFilterText(e.target.value)}
    />;
  }, [filterText, resetPaginationToggle]);

    useEffect(() => {
      const fetchApplications = async () => {
        try {
          const applicationData = await getApplications();
          if (applicationData?.data) {
            setApplications(applicationData.data);
          }
        } catch (error) {
          console.error("Failed to fetch candidates", error);
        }
      };
  
      fetchApplications();
    }, []);

  return (
    <DataTable
      title="Applications"
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


export default Candidate;