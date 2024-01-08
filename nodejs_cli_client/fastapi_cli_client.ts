import axios from 'axios';

const API_URL = 'http://localhost:8000'; // replace with your API URL

type TODO = {
	id: number;
	title: string;
	description: string;
	completed: boolean;
};

async function getTodos() {
	try {
		const response = await axios.get(`${API_URL}/todos`);
		const todos = response.data;
		todos.forEach((todo: TODO) => {
			console.log(
				`ID: ${todo.id}, Title: ${todo.title}, Completed: ${todo.completed}`
			);
		});
	} catch (error) {
		console.error(error);
	}
}

async function getTodo({ id: todoId }: Pick<TODO, 'id'>) {
	try {
		const response = await axios.get(`${API_URL}/todos/${todoId}`);
		const todo = response.data;
		console.log(
			`ID: ${todo.id}, Title: ${todo.title}, Completed: ${todo.completed}`
		);
	} catch (error) {
		console.error(error);
	}
}

async function createTodo({
	completed,
	title,
	description,
}: Pick<TODO, 'title' | 'description' | 'completed'>) {
	try {
		const todo = { title, description, completed };
		const response = await axios.post(`${API_URL}/todos`, todo);
		if (response.status === 201) {
			console.log('Todo created successfully');
		}
	} catch (error) {
		console.error(error);
	}
}

async function updateTodo({ completed, description, id: todoId, title }: TODO) {
	try {
		const todo = { title, description, completed };
		const response = await axios.put(`${API_URL}/todos/${todoId}`, todo);
		if (response.status === 200) {
			console.log('Todo updated successfully');
		}
	} catch (error) {
		console.error(error);
	}
}

async function deleteTodo({ id: todoId }: Pick<TODO, 'id'>) {
	try {
		const response = await axios.delete(`${API_URL}/todos/${todoId}`);
		if (response.status === 204) {
			console.log('Todo deleted successfully');
		}
	} catch (error) {
		console.error(error);
	}
}

(async () => {
	console.log('Get all todos');
	await getTodos();

	console.log('\nGet a todo');
	await getTodo({
		id: 27,
	});

	console.log('\nCreate a todo');
	await createTodo({
		title: 'Node JS New Todo',
		description: 'This is a node JS new todo',
		completed: false,
	});

	console.log('\nTodos after creating a new todo');
	await getTodos();

	console.log('\nUpdate a todo');
	await updateTodo({
		id: 27,
		title: 'Node JS Updated Todo',
		description: 'This is a node JS updated todo',
		completed: true,
	});

	console.log('\nDeleting a todo');
	await deleteTodo({ id: 27 });
})();
