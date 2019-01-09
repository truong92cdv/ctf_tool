#include <Python.h>
#include <arpa/inet.h>
#include <openssl/md5.h>

static PyObject *HashExtError;

static PyObject *hashext_md5(PyObject *self, PyObject *args, PyObject *kwargs) {
    static char *keywords[] = {"data", "sign", "length", "append", NULL};
    static char hex[] = "0123456789abcdef";

    char *data, *sign, *append;
    unsigned char digest[MD5_DIGEST_LENGTH];
    unsigned int h[4];
    int i, n, len, cnt, ok;
    MD5_CTX ctx;
    PyObject *ret;

    if (!PyArg_ParseTupleAndKeywords(args, kwargs, "ssis", keywords, &data, &sign, &len, &append))
        return NULL;
    if (len <= 0) {
        PyErr_SetString(HashExtError, "Wrong salt length");
        return NULL;
    }
    if (strlen(sign) != 2 * MD5_DIGEST_LENGTH)  {
        PyErr_SetString(HashExtError, "Wrong signature");
        return NULL;
    }

    cnt = len + strlen(data);
    n = cnt + 1;
    ok = 64 - (n & 0x3f);
    if (ok < 8)
        n += 64;
    n += ok;

    char *new_data = (char *) malloc(n + strlen(append) + 1);
    char *new_sign = (char *) malloc(2 * MD5_DIGEST_LENGTH + 1);
    if (new_sign == NULL || new_data == NULL)
        return PyErr_NoMemory();

    memset(new_data, 0, n + 1);
    memcpy(new_data + len, data, strlen(data));
    new_data[cnt] = 0x80;
    cnt <<= 3;
    new_data[n - 8] = cnt;
    new_data[n - 7] = cnt >> 8;
    new_data[n - 6] = cnt >> 16;
    new_data[n - 5] = cnt >> 24;
    memcpy(new_data + n, append, strlen(append));

    MD5_Init(&ctx);
    MD5_Update(&ctx, new_data, n);

    sscanf(sign, "%08x%08x%08x%08x", &h[0], &h[1], &h[2], &h[3]);
    ctx.A = htonl(h[0]);
    ctx.B = htonl(h[1]);
    ctx.C = htonl(h[2]);
    ctx.D = htonl(h[3]);

    MD5_Update(&ctx, append, strlen(append));
    MD5_Final(digest, &ctx);

    for (i = 0; i < MD5_DIGEST_LENGTH; i++) {
        new_sign[2 * i] = hex[digest[i] >> 4];
        new_sign[2 * i + 1] = hex[digest[i] & 0xF];
    }
    new_sign[2 * MD5_DIGEST_LENGTH] = 0;
    
    ret = PyTuple_Pack(2, PyString_FromStringAndSize(new_data + len, n - len + strlen(append)), PyString_FromString(new_sign));
    free(new_data);
    free(new_sign);
    return ret;
}

static PyMethodDef HashExtMethods[] = {
    { "md5", (PyCFunction)hashext_md5, METH_VARARGS | METH_KEYWORDS, "Implement md5 attack" },
    { NULL, NULL, 0, NULL }
};

PyMODINIT_FUNC inithashext(void) {
    PyObject *module;

    module = Py_InitModule("hashext", HashExtMethods);
    if (module == NULL)
        return;

    HashExtError = PyErr_NewException("hashext.error", NULL, NULL);
    Py_INCREF(HashExtError);
    PyModule_AddObject(module, "error", HashExtError);
}
