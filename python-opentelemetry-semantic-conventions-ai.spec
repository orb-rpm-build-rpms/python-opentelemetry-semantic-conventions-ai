Name:           python-opentelemetry-semantic-conventions-ai
Version:        0.5.1
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        OpenTelemetry Semantic Conventions Extension for Large Language Models

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        Apache-2.0
URL:            ...
Source:         %{pypi_source opentelemetry_semantic_conventions_ai}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'opentelemetry-semantic-conventions-ai' generated automatically by pyp2spec.}

%description %_description

%package -n     python3-opentelemetry-semantic-conventions-ai
Summary:        %{summary}

%description -n python3-opentelemetry-semantic-conventions-ai %_description


%prep
%autosetup -p1 -n opentelemetry_semantic_conventions_ai-%{version}


%generate_buildrequires
%pyproject_buildrequires


%build
%pyproject_wheel


%install
%pyproject_install
# Automatically extracted from wheel
%pyproject_save_files opentelemetry


%check
%pyproject_check_import


%files -n python3-opentelemetry-semantic-conventions-ai -f %{pyproject_files}


%changelog
%autochangelog
