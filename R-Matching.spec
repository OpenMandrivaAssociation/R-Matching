%global packname  Matching
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          4.8_3.1
Release:          1
Summary:          Multivariate and Propensity Score Matching with Balance Optimization
Group:            Sciences/Mathematics
License:          GPLv3
URL:              http://cran.r-project.org/web/packages/Matching/index.html
Source0:          http://cran.r-project.org/src/contrib/Matching_4.8-3.1.tar.gz
BuildRequires:    R-devel R-MASS R-rgenoud R-graphics R-stats R-parallel R-grDevices
Requires:         R-core R-MASS R-rgenoud R-graphics R-stats R-parallel R-grDevices

%description
Provides functions for multivariate and propensity score matching and for
finding optimal balance based on a genetic search algorithm. A variety of
univariate and multivariate metrics to determine if balance has been
obtained are also provided.

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/DESCRIPTION
%doc %{rlibdir}/%{packname}/CITATION
%doc %{rlibdir}/%{packname}/html
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/demo
%{rlibdir}/%{packname}/extras
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/help