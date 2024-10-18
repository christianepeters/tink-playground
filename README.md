# Tink Playground

Objective: Try out Tink library.

## Resources

* [Tink for Python How-To](https://android.googlesource.com/platform/external/tink/+/HEAD/docs/PYTHON-HOWTO.md)
* [Getting Started Overview | Tink](https://developers.google.com/tink/getting-started)
* [Project IDX](https://idx.google.com/)


## Setup

1. Set up workspace in Google IDX, e.g., 
https://idx.google.com/tink-RANDOMNUMBER

    See also [Python project in Google IDX](https://github.com/christianepeters/howto/blob/master/projectidx.md).

2. Activate environment
    ```
    python3 -m venv env
    pip3 --version
    source env/bin/activate
    ```

3. Install Tink

    ```
    pip3 install tink==1.10.0
    ```

4. Write your first test program, e.g., [aead-test.py](src/aead.py).

