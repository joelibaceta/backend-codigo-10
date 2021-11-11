import React from "react";

import {Modal, ModalBody, ModalFooter, ModalHeader} from "reactstrap"

export default function NewItemModal({cancelCallback}) {
    return (
        <Modal isOpen={true}>
            <ModalHeader>
                Agregar Tarea
            </ModalHeader>

            <ModalBody>
                <div className="add-item-form">
                    <div className="form-group">
                        <input   
                            className="form-control" 
                            type="text"
                            id="addItemInput"
                        />
                    </div>
                </div>
            </ModalBody>
            <ModalFooter>
                <button className="btn btn-success">Agregar</button>
                <button className="btn btn-danger" onclick={cancelCallback}>Cancelar </button>
            </ModalFooter>
        </Modal>
    )
}

