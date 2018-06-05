# PDF to semantic HTML conversion

Transcript contains Python programs whose job is to translate PDFs into semantic HTML.

`pdf2html.py`: Batch process a folder full of PDFs ready for `transcript.py`

`transcript.py`: Get semantic HTML from PDFs converted by pdf2htmlEX.

`ttf.py`: Recover lost text from PDFs where characters are nothing more than images of themselves.


# Install

Requires Python 3.

[pdf2htmlEX](https://github.com/coolwanglu/pdf2htmlEX) install:

* Install [Docker](https://www.docker.com/community-edition#/download) and [allow running without sudo](https://askubuntu.com/questions/477551/how-can-i-use-docker-without-sudo)
* Create a local alias for docker command by adding the following to `~/.bash_aliases`:

    alias pdf2htmlEX='docker run -ti --rm -v "${PWD}":/pdf bwits/pdf2htmlex pdf2htmlEX'

* Test: `pdf2htmlEX "test.pdf"`

Install dependencies:

    sudo pip3 install -r requirements.txt



# Configure

Configure the `DATA_DIR` in `config.py`.
Place our PDFs in this directory.
Final products will appear with a `.htm` extension.



# Run

`./pdf2html.py`
`./transcript.py`

When you change configuration or tweak some code, you only need to run `./transcript.py`.
