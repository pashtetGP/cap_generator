!This file is subject to the terms and conditions defined in
!file 'LICENSE.txt', which is part of this source code package.

TITLE
    
	CAP_extensive_form_cap134_5;

STOCHASTIC

DATA
	
	I := DATAFILE("cap134_5_SETS.dat");
	J := DATAFILE("cap134_5_SETS.dat");
	K := DATAFILE("cap134_5_SETS.dat");				! - num scenarios
	Q := I;							! - num 1st stage columns
	T := I*J;						! - num 2nd stage columns
	R := J+I;						! - num rows in T and W
	

SCENARIO
    
	k := 1..K;

INDEX
	FirstStCol := 1..Q;
	SecondStCol := 1..T;
	Row := 1..R;	

PROBABILITIES
    
	p[k] :=  ALLEQUAL;

RANDOM DATA

	Vector_h[k, Row] := DATAFILE("cap134_5_RANDOM.dat");	! - rows are related to scenarios

DATA
    
	Vector_c[FirstStCol] := DATAFILE("cap134_5_DATA.dat");
	Vector_d[SecondStCol] := DATAFILE("cap134_5_DATA.dat");
	Vector_b := DATAFILE("cap134_5_DATA.dat");			! - max sum of h over all scenarios
	Matrix_A[FirstStCol] := DATAFILE("cap134_5_DATA.dat");
	Matrix_T[Row, FirstStCol] := DATAFILE("cap134_5_DATA.dat");
	Matrix_W[Row, SecondStCol] := DATAFILE("cap134_5_DATA.dat");
	x_ub[FirstStCol] := DATAFILE("cap134_5_DATA.dat");

STAGE1 BINARY VARIABLES

	x[FirstStCol];

STAGE2 VARIABLES

	y[SecondStCol];

MACROS

	StageFirst = sum(FirstStCol: Vector_c * x);
	StageSecond = sum(SecondStCol: Vector_d * y);

MIN

	Objective = StageFirst + StageSecond;

SUBJECT TO
	
	FirstStCnstr: sum(FirstStCol: Matrix_A * x) >= Vector_b;
    	SecondStCnstr[Row]: sum(FirstStCol: Matrix_T * x) + sum(SecondStCol: Matrix_W * y) >= Vector_h;

BOUNDS

	BinBounds[FirstStCol]: x <= x_ub;	! - why do we need it

END