#include <math.h>
#include <complex.h>
#include <stdlib.h>
#include <stdio.h>

#define TABLE_LENGTH pow(2, 16)
#define DENSITY 0.0075
#define RIGIDITY 52500000.0
#define DAMPER 0.0003


// time
double *linspace(int table_length) {
	int L = table_length+1;
	int l = 0;
	int d = 1.0;

	double *t = calloc(L, sizeof(double));
	double step = (d - l) / (double)(L - 1);
	for (int n = 0; n < L; n++) t[n] = (l + ((double)n*step));
	return t;
}

// volume
double volume(double length, double width, double depth) {
	return length*width*depth;
}

// mass
double mass(double volume, double density) {
	return volume*density;
}

// spring constant
double k(double G, double volume, double length) {
	double u = G*volume;
	double v = pow(length, 2);

	return u/v;
}

// root 1
double alpha(double m, double b) {
	return -b/(2.0*m);
}

// root 2
double beta(double m, double b, double k) {
	double discriminant = sqrt((4*m*k - pow(b, 2)));
	return discriminant/(2.0*m);
}

// period
double period(double b) {
	return (2.0*M_PI)/b;
}

// frequency
double frequency(double T) {
	return 1.0/T;
}

int main() {
	double l = 128;
	double w = 100.0/15.0;
	double d = 1.0;

	double v = volume(l, w, d);

	double m = mass(v, DENSITY);
	double K = k(RIGIDITY, v, l);

	double a = alpha(m, DAMPER);
	double b = beta(m, DAMPER, K);

	//TODO: parameterize amplitude with displacement (in mm)
	double A = 1;

	// TODO: move this to its own function
	double *t = linspace(TABLE_LENGTH);
	for (int n; n<TABLE_LENGTH+1; n++) {
		t[n] = A*exp(a*n)*sin(b*n);
		printf("%d %lf\n", n, t[n]);
	}

	return 0;

}
