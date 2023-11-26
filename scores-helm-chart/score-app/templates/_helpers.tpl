{{/*
Create a default fully qualified app name.
We truncate at 63 chars because some Kubernetes name fields are limited to this (by the DNS naming spec).
If the release name contains the chart name, it will be used as a full name.
*/}}
{{- define "flaskapp.fullname" -}}
{{- printf "%s-%s" .Release.Name "flaskapp" | trunc 63 | trimSuffix "-" }}
{{- end -}}

{{- define "flaskapp.name" -}}
{{- include "flaskapp.nameOverride" . | default .Chart.Name }}
{{- end -}}

{{- define "flaskapp.nameOverride" -}}
{{- end -}}

{{/*
Labels used for flaskapp resources.
*/}}
{{- define "flaskapp.labels" -}}
  app.kubernetes.io/name: {{ include "flaskapp.name" . }}
  app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Common labels used for resources.
*/}}
{{- define "labels.standard" -}}
  app.kubernetes.io/name: {{ include "flaskapp.name" . }}
  app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}

{{/*
Selector labels for flaskapp resources.
*/}}
{{- define "flaskapp.selectorLabels" -}}
  app.kubernetes.io/name: {{ include "flaskapp.name" . }}
  app.kubernetes.io/instance: {{ .Release.Name }}
{{- end }}
