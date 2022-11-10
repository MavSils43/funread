import React, { useState } from "react";
import "./AddPage.css";
import DashHeader from "../HeaderDashboard/HeaderDashboard";
import { Button } from "react-bootstrap";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faX } from "@fortawesome/free-solid-svg-icons";
import { useNavigate } from "react-router-dom";
import BookPages from "../BookPages/BookPages";

function AddPage(props) {
  const [myBookName, setMyBookName] = useState("New Book Name");
  const navigate = useNavigate();

  const closeAddPage = () => {
    navigate("/mylibrary");
  };

  return (
    <div className="add-page-container">
      <div className="add-page-header">
        <DashHeader />
      </div>
      <div className="add-page-body">
        <div className="add-page-banner">
          <p className="add-page-banner-title">{myBookName}</p>
          <div className="add-page-banner-buttons-container">
            <Button
              variant="outline-dark"
              size="md"
              className="add-page-banner-option-button"
              type="button"
            >
              PRESENT
            </Button>
            <Button
              variant="outline-dark"
              size="md"
              className="add-page-banner-option-button"
              type="button"
            >
              SAVE
            </Button>
            <Button
              variant="outline-dark"
              className="add-page-banner-close-button"
              style={{ marginRight: 20 }}
              type="button"
              onClick={closeAddPage}
            >
              <FontAwesomeIcon icon={faX} />
            </Button>
          </div>
        </div>
        <div className="add-page-book-information-container">
          <div className="add-page-pages-container">
            <BookPages />
          </div>
          <div className="add-page-preview-container"></div>
          <div className="add-page-template-widget-container"></div>
        </div>
      </div>
    </div>
  );
}

export default AddPage;