<<<<<<< HEAD
#include "Python.h"

/**
 * print_python_string - Prints information about Python strings.
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	long int length;

	fflush(stdout);

	printf("[.] string object info\n");
	if (strcmp(p->ob_type->tp_name, "str") != 0)
=======
#include <stdio.h>
#include <string.h>
#include <Python.h>

/**
 * print_python_string - Prints string information
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_string(PyObject *p)
{

	PyObject *str, *repr;

	(void)repr;
	printf("[.] string object info\n");

	if (strcmp(p->ob_type->tp_name, "str"))
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
	{
		printf("  [ERROR] Invalid String Object\n");
		return;
	}

<<<<<<< HEAD
	length = ((PyASCIIObject *)(p))->length;

=======
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
	if (PyUnicode_IS_COMPACT_ASCII(p))
		printf("  type: compact ascii\n");
	else
		printf("  type: compact unicode object\n");
<<<<<<< HEAD
	printf("  length: %ld\n", length);
	printf("  value: %ls\n", PyUnicode_AsWideCharString(p, &length));
=======

	repr = PyObject_Repr(p);
	str = PyUnicode_AsEncodedString(p, "utf-8", "~E~");
	printf("  length: %ld\n", PyUnicode_GET_SIZE(p));
	printf("  value: %s\n", PyBytes_AsString(str));
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
}
