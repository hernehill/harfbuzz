name = "harfbuzz"

version = "8.2.1.hh.1.0.0"

authors = [
    "Harfbuzz",
]

description = """Opentype"""

with scope("config") as c:
    import os

    c.release_packages_path = os.environ["HH_REZ_REPO_RELEASE_EXT"]
    # c.build_thread_count = 1

requires = [
    "freetype",
    "libpng",
]

private_build_requires = []

variants = []


def commands():
    env.REZ_HARFBUZZ_ROOT = "{root}"
    env.HARFBUZZ_ROOT = "{root}"
    env.HARFBUZZ_LOCATION = "{root}"
    env.HARFBUZZ_INCLUDE_DIR = "{root}/include"
    env.HARFBUZZ_LIBRARY_DIR = "{root}/lib64"

    env.PATH.append("{root}/lib64")
    env.LD_LIBRARY_PATH.append("{root}/lib64")
    env.PKG_CONFIG_PATH.append("{root}/lib64/pkgconfig")


uuid = "repository.harfbuzz"
