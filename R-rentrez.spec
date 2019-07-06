#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-rentrez
Version  : 1.2.2
Release  : 14
URL      : https://cran.r-project.org/src/contrib/rentrez_1.2.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/rentrez_1.2.2.tar.gz
Summary  : 'Entrez' in R
Group    : Development/Tools
License  : MIT
Requires: R-XML
Requires: R-httr
Requires: R-jsonlite
BuildRequires : R-XML
BuildRequires : R-httr
BuildRequires : R-jsonlite
BuildRequires : buildreq-R

%description
allowing users to search databases like 'GenBank'

%prep
%setup -q -c -n rentrez

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1556823346

%install
export SOURCE_DATE_EPOCH=1556823346
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rentrez
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rentrez
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library rentrez
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc rentrez || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/rentrez/CITATION
/usr/lib64/R/library/rentrez/DESCRIPTION
/usr/lib64/R/library/rentrez/INDEX
/usr/lib64/R/library/rentrez/LICENSE
/usr/lib64/R/library/rentrez/Meta/Rd.rds
/usr/lib64/R/library/rentrez/Meta/features.rds
/usr/lib64/R/library/rentrez/Meta/hsearch.rds
/usr/lib64/R/library/rentrez/Meta/links.rds
/usr/lib64/R/library/rentrez/Meta/nsInfo.rds
/usr/lib64/R/library/rentrez/Meta/package.rds
/usr/lib64/R/library/rentrez/Meta/vignette.rds
/usr/lib64/R/library/rentrez/NAMESPACE
/usr/lib64/R/library/rentrez/NEWS
/usr/lib64/R/library/rentrez/R/rentrez
/usr/lib64/R/library/rentrez/R/rentrez.rdb
/usr/lib64/R/library/rentrez/R/rentrez.rdx
/usr/lib64/R/library/rentrez/doc/index.html
/usr/lib64/R/library/rentrez/doc/rentrez_tutorial.R
/usr/lib64/R/library/rentrez/doc/rentrez_tutorial.Rmd
/usr/lib64/R/library/rentrez/doc/rentrez_tutorial.html
/usr/lib64/R/library/rentrez/help/AnIndex
/usr/lib64/R/library/rentrez/help/aliases.rds
/usr/lib64/R/library/rentrez/help/paths.rds
/usr/lib64/R/library/rentrez/help/rentrez.rdb
/usr/lib64/R/library/rentrez/help/rentrez.rdx
/usr/lib64/R/library/rentrez/html/00Index.html
/usr/lib64/R/library/rentrez/html/R.css
/usr/lib64/R/library/rentrez/tests/test-all.R
/usr/lib64/R/library/rentrez/tests/testthat/test_api_key.r
/usr/lib64/R/library/rentrez/tests/testthat/test_citmatch.r
/usr/lib64/R/library/rentrez/tests/testthat/test_docs.r
/usr/lib64/R/library/rentrez/tests/testthat/test_fetch.r
/usr/lib64/R/library/rentrez/tests/testthat/test_httr.r
/usr/lib64/R/library/rentrez/tests/testthat/test_httr_post.r
/usr/lib64/R/library/rentrez/tests/testthat/test_info.r
/usr/lib64/R/library/rentrez/tests/testthat/test_link.r
/usr/lib64/R/library/rentrez/tests/testthat/test_net.r
/usr/lib64/R/library/rentrez/tests/testthat/test_parse.r
/usr/lib64/R/library/rentrez/tests/testthat/test_post.r
/usr/lib64/R/library/rentrez/tests/testthat/test_query.r
/usr/lib64/R/library/rentrez/tests/testthat/test_search.r
/usr/lib64/R/library/rentrez/tests/testthat/test_summary.r
/usr/lib64/R/library/rentrez/tests/testthat/test_webenv.r
