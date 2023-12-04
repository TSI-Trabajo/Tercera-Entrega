/** @odoo-module **/    

import { registry } from '@web/core/registry';
const { Component, useState, onWillStart, useRef } = owl;
import { useService } from "@web/core/utils/hooks";

class COMP1Componente extends Component {
    setup() {
        this.state = useState({
            taskList:[],
            isEdit: true,
            activeId: false,
        })
        this.orm = useService("orm")
        this.searchInput = useRef("search-input")

        onWillStart(async ()=>{
            await this.getAllTasks()
        })
    }

    async getAllTasks(){
        this.state.taskList = await this.orm.searchRead(this.model, [], )
    }

    addTask(){
        this.resetForm()
        this.state.activeId = false
        this.state.isEdit = false
    }

    editTask(task){
        this.state.activeId = task.id
        this.state.isEdit = true
        this.state.task = {...task}
    }

    async saveTask(){

        if (!this.state.isEdit){
            await this.orm.create(this.model, [this.state.task])
            this.resetForm()
        } else {
            await this.orm.write(this.model, [this.state.activeId], this.state.task)
        }
        $('#exampleModal').modal('hide')
        this.resetForm()
        await this.getAllTasks()
    }

    resetForm(){
        this.state.task = {name:""}
    }

    async deleteTask(task){
        await this.orm.unlink(this.model, [task.id])
        await this.getAllTasks()
    }

    async searchTasks(){
        const text = this.searchInput.el.value
    }

    async updatePrecio(e, task){
        await this.orm.write(this.model, [task.id], {precio: e.target.value})
        await this.getAllTasks()
    }  

}
    
COMP1Componente.template = 'owl.COMP1Componente';
registry.category('actions').add('owl.action_COMP1Componente_js', COMP1Componente);