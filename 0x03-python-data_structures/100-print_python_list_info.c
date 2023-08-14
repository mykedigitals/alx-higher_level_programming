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
	int qtty, designate, pik;
	PyObject *maat;

	qtty = Py_SIZE(p);
	designate = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", qtty);
	printf("[*] Allocated = %d\n", designate);

	for (pik = 0; pik < qtty; pik++)
	{
		printf("Element %d: ", pik);
		maat = PyList_GetItem(p, pik);
		printf("%s\n", Py_TYPE(maat)->tp_name);
	}
}
