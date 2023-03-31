<<<<<<< HEAD
#include <Python.h>
#include <stdio.h>
/**
 * print_python_float - gives data of the PyFloatObject
 * @p: the PyObject
 */
void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}
	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}
/**
 * print_python_bytes - gives data of the PyBytesObject
 * @p: the PyObject
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0, i = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");
	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = (assert(PyBytes_Check(p)), (((PyBytesObject *)(p))->ob_sval));
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
	while (i < size + 1 && i < 10)
	{
		printf(" %02hhx", string[i]);
		i++;
	}
	printf("\n");
}
/**
 * print_python_list - gives data of the PyListObject
 * @p: the PyObject
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;
	int i = 0;

	fflush(stdout);
	printf("[*] Python list info\n");
	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);
		while (i < size)
		{
			item = PyList_GET_ITEM(p, i);
			printf("Element %d: %s\n", i, item->ob_type->tp_name);
			if (PyBytes_Check(item))
				print_python_bytes(item);
			else if (PyFloat_Check(item))
				print_python_float(item);
			i++;
		}
	}
	else
		printf("  [ERROR] Invalid List Object\n");
=======
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <float.h>
#include <sys/types.h>
#include <python3.4/Python.h>
#include <python3.4/object.h>
#include <python3.4/listobject.h>
#include <python3.4/floatobject.h>
#define PY_SSIZE_T_CLEAN

/**
* print_python_bytes - Prints some basic info about a Python bytes object
* @p: A pointer to the Python bytes object
*/

void print_python_bytes(PyObject *p)
{
	int i, bytes_len, n, error = 1;

	fflush(stdout);
	printf("[.] bytes object info\n");
	fflush(stdout);
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "bytes") == 0))
	{
		bytes_len = (int)(((PyVarObject *)p)->ob_size);
		n = bytes_len < 10 ? bytes_len : 9;
		printf("  size: %d\n", bytes_len);
		fflush(stdout);
		printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);
		fflush(stdout);
		if ((n > 0) && (((PyBytesObject *)p)->ob_sval != NULL))
		{
			printf("  first %d bytes:", n + 1);
			fflush(stdout), error = 0;
			for (i = 0; i < n + 1; i++)
			{
				printf(" %02x", (unsigned char)*(((PyBytesObject *)p)->ob_sval + i));
				fflush(stdout);
			}
			printf("\n");
			fflush(stdout);
		}
	}
	if (error)
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		fflush(stdout);
	}
}

/**
 * print_python_float - Prints some basic info about a Python float object
 * @p: A pointer to the Python float object
 */
void print_python_float(PyObject *p)
{
	double val;
	char *buf = NULL;

	fflush(stdout);
	printf("[.] float object info\n");
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "float") == 0))
	{
		val = ((PyFloatObject *)p)->ob_fval;
		buf = PyOS_double_to_string(val, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
		printf("  value: %s\n", buf);
		fflush(stdout);
	}
	else
	{
		printf("  [ERROR] Invalid Float Object\n");
		fflush(stdout);
	}
}

/**
 * print_python_list - Prints some basic info about a Python list object
 * @p: A pointer to the Python list object
 */
void print_python_list(PyObject *p)
{
	int i, list_len;
	PyObject *item = NULL;

	fflush(stdout);
	printf("[*] Python list info\n");
	fflush(stdout);
	if ((p != NULL) && (p->ob_type != NULL)
		&& ((p->ob_type)->tp_name != NULL)
		&& (strcmp((p->ob_type)->tp_name, "list") == 0))
	{
		list_len = (int)(((PyVarObject *)(p))->ob_size);
		printf("[*] Size of the Python List = %d\n", list_len);
		fflush(stdout);
		printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);
		fflush(stdout);
		for (i = 0; (((PyListObject *)p)->ob_item != NULL) && (i < list_len); i++)
		{
			item = (PyObject *)*(((PyListObject *)p)->ob_item + i);
			printf("Element %d: %s\n", i, (item->ob_type)->tp_name);
			fflush(stdout);
			if ((item != NULL) && (item->ob_type != NULL)
				&& ((item->ob_type)->tp_name != NULL)
				&& (strcmp((item->ob_type)->tp_name, "bytes") == 0))
			{
				print_python_bytes(item);
			}
			else if ((item != NULL) && (item->ob_type != NULL)
				&& ((item->ob_type)->tp_name != NULL)
				&& (strcmp((item->ob_type)->tp_name, "float") == 0))
			{
				print_python_float(item);
			}
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
		fflush(stdout);
	}
>>>>>>> 2276ad50c30a4f134bae58729cfd329eeb95acb3
}
