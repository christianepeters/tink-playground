# Tink Playground

Objective: Try out Tink library.

## Resources

* [Tink for Python How-To](https://fuchsia.googlesource.com/third_party/tink/+/refs/tags/v1.4.0-rc1/docs/PYTHON-HOWTO.md)
* [Getting Started Overview | Tink](https://developers.google.com/tink/getting-started)
* [Project IDX](https://idx.google.com/)


## Steps

1. Set up workspace in Google IDX, e.g., 
https://idx.google.com/tink-RANDOMNUMBER

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

