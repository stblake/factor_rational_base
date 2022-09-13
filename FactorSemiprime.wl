(* ::Package:: *)

ClearAll[FactorSemiprime];

Options[FactorSemiprime] = {"FactorSemiprimeMessages" -> False,"InitialBase" -> 3, "SpecificBase" -> 1};

FactorSemiprime::SpecificBaseMalformed="SpecificBase should be greater than 1.";
FactorSemiprime::InitialBaseNonInteger = "InitialBase should be an integer.";
FactorSemiprime::InitialBaseTooSmall = "InitialBase should be at least three.";

FactorSemiprime[\[ScriptCapitalN]_Integer, OptionsPattern[]]:=Module[
{print, j, a, b, partitions, fac},

If[\[ScriptCapitalN]<2 || !IntegerQ[\[ScriptCapitalN]] || PrimeQ[\[ScriptCapitalN]], 
	Return[1]];

print = If[OptionValue["FactorSemiprimeMessages"]//TrueQ,
	Print,
	Identity
];

If[OptionValue["SpecificBase"] != 1,
	If[OptionValue["SpecificBase"] <= 1,
		Message[FactorSemiprime::SpecificBaseMalformed];
		Return[1, Module]];
	{a, b} = NumeratorDenominator @ OptionValue["SpecificBase"];
	Return[factor[\[ScriptCapitalN],a,b,print], Module]
];

j = OptionValue["InitialBase"];

If[!IntegerQ[j],
	Message[FactorSemiprime::InitialBaseNonInteger];
	Return[1]
];

If[j<3, 
	Message[FactorSemiprime::InitialBaseTooSmall];
	Return[1]
];

While[True,
	print[Style[j,30]];
	partitions = Union[Sort /@ IntegerPartitions[j,{2}]];
	Do[
		{b,a} = pt;
		If[a > b && CoprimeQ[a,b],
			print[Style[{a,b},Gray]];
			fac=factor[\[ScriptCapitalN],a,b,print];
			If[fac!=1,
				print[{a,b}];
				Return[fac, Module]
			]
		],
	{pt, partitions}];
	j++
];
1
]


ClearAll[factor];

factor[\[ScriptCapitalN]_Integer, a_Integer, b_Integer, print_] := Module[
{q = \[ScriptCapitalN], gcd, ngcd = 0, ndivs = 0},

While[True,
	ndivs++;
	q = Quotient[b q,a];

	If[q < 2, 
		Return[1, Module]];

	Do[
		ngcd++;
		gcd = GCD[q^2 - k^2, \[ScriptCapitalN]];
		If[TrueQ[gcd != 1 && gcd != \[ScriptCapitalN]],
			print[Row @ {"k = ", k, ", q = ", q, ", ngcd = ", ngcd, ", ndivs = ", ndivs}];
			Return[gcd, Module]
		],
	{k, 0, 1 + Ceiling[Log[2, ndivs]]}]
];
1
]
