/*
 * 100-print_python_list_info.c
 */

#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 */

void print_python_list_info(PyObject *p)
{
	int qtty, alloc, i;
	PyObject *maat;

	qtty = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", qtty);
	printf("[*] Allocated = %d\n", alloc);

	for (i = 0; i < qtty; i++)
	{
		printf("Element %d: ", i);
		maat = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(maat)->tp_name);
	}
}
